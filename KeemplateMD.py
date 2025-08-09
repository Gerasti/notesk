import sys
from functools import reduce

# For work use 'input_data' in 'main'

# Input:
# ff Example ct work

# CTRL + D or CTRL + Z

# Output:
#<details>
#<summary> Example  </summary>     <!-- ff -->
#
#> work <!-- Citation -->
#
#</details>             <!-- FFIELD -->


KEYS_LIST = ['-', '--']
KEYS = ['ff', 'tp', 'pf', 'ce', 'ac', 'gc', 'lt', 'sc', 'ct', 'hl']
LIMIT_keys_at_gc = 1

def tokenize_input(input_str):
    word = ""
    tokens = []
    for char in input_str:
        if char.isspace():
            if word:
                tokens.append(word)
                word = ""
            tokens.append(char)
        else:
            word += char
    if word:
        tokens.append(word)
    return tokens

def clean_data(data):
    data = [d for d in data if d not in {" ", "\n"}]
    if data and data[0].startswith(' '):
        data = data[1:]
    if data and (data[-1].endswith(' ') or data[-1].endswith('\n')):
        data = data[:-1]
    return data

def format_output(key, data, context):
    data = clean_data(data)
    ctx = context.copy()

    if all(not (s.strip()) for s in data):
        if key == 'gc':
            ctx['NEST_gc'] = True
            return "\n<details>\n<summary> manual </summary> <!-- gc -->\n\n<!-- GENERAL COMMENT -->\n\n ", ctx
        elif key == 'lt':
            ctx['MODE_list_lt'] = True
            return None, ctx
        elif key == 'hl':
            return "---", ctx
        print(f"[DEBUG] Key '{key}' without data")
        return None, ctx

    joined = ''.join(data)

    if ctx['MODE_list_lt']:
        if key == '-':
            return f"- {joined} <!-- JUST -->", ctx
        elif key == '--':
            return f"    - {joined} <!-- SPACE -->", ctx
        return None, ctx

    if key == 'ff':
        ctx['open_ff'] += 1
        return f"<details>\n<summary> {joined}  </summary>     <!-- ff -->", ctx
    elif key == 'tp':
        ctx['open_tp'] += 1
        ctx['include_tp'] = True
        return f"\n<details>\n<summary> {joined}  </summary> <!-- tp -->", ctx
    elif key == 'pf':
        return f"\n### +/ {joined} <!-- PLATFORM -->", ctx
    elif key == 'ce':
        return f"<!-- CODE -->\n\n```MarkDown Keemplate\n{joined}\n```\n<!-- CODE -->", ctx
    elif key == 'ac':
        return f"\n#### {joined} <!-- ACTION -->", ctx
    elif key == 'gc':
        ctx['NEST_gc'] = True
        ctx['keys_at_gc'] += 1
        return f"\n<details>\n<summary> manual </summary> <!-- gc -->\n\n<!-- GENERAL COMMENT -->\n\n##### {joined}", ctx
    elif key == 'sc':
        return f"\n![image]({joined}) <!-- SCREEN -->", ctx
    elif key == 'lt':
        ctx['MODE_list_lt'] = True
        return f"\n### {joined} <!-- LIST -->", ctx
    elif key == 'ct':
        return f"\n> {joined} <!-- Citation -->", ctx
    elif key == 'hl':
        return "---", ctx

    return None, ctx

def process_tokens(tokens):
    output = []
    context = {
        'MODE_list_lt': False,
        'NEST_gc': False,
        'open_ff': 0,
        'open_tp': 0,
        'include_tp': False,
        'keys_at_gc': 0,
    }

    current_key = None
    start_idx = 0

    def close_open_blocks(ctx, token):
        out = []
        if ctx['NEST_gc'] and (ctx['keys_at_gc'] == LIMIT_keys_at_gc or token in {'ff', 'tp', 'gc'}):
            out.append('\n<!--  GENERAL COMMENT -->\n\n</details> <!-- COMMENT -->\n')
            ctx['NEST_gc'] = False
            ctx['keys_at_gc'] = 0
        if token == 'ff':
            if ctx['include_tp']:
                out.append('\n</details>            <!-- TOPIC -->\n')
                ctx['open_tp'] -= 1
                ctx['include_tp'] = False
                while ctx['open_ff'] > 0:
                    out.append('\n</details>            <!-- FFIELD -->\n')
                    ctx['open_ff'] -= 1
        elif token == 'tp':
            if ctx['include_tp']:
                out.append('\n</details> <!-- TOPIC -->\n')
                ctx['open_tp'] -= 1
                ctx['include_tp'] = False
        return out, ctx

    idx = 0
    while idx < len(tokens):
        token = tokens[idx]
        if token in KEYS or (token in KEYS_LIST and (context['MODE_list_lt'] or current_key == 'lt')):
            if current_key is not None:
                data = tokens[start_idx + 1:idx]
                formatted, context = format_output(current_key, data, context)
                if formatted:
                    output.append(formatted)
                closed_blocks, context = close_open_blocks(context, token)
                output.extend(closed_blocks)

            current_key = token
            start_idx = idx
        idx += 1

    # last block
    if current_key:
        data = tokens[start_idx + 1:]
        formatted, context = format_output(current_key, data, context)
        if formatted:
            output.append(formatted)

    # closing unblocked nest
    while context['NEST_gc']:
        output.append('\n<!-- GENERAL COMMENT -->\n\n</details> <!-- COMMENT -->\n')
        context['NEST_gc'] = False

    while context['open_tp'] > 0:
        output.append('\n</details>            <!-- TOPIC -->')
        context['open_tp'] -= 1
        context['include_tp'] = False

    while context['open_ff'] > 0:
        output.append('\n</details>             <!-- FFIELD -->')
        context['open_ff'] -= 1


    return output

if __name__ == "__main__":
    input_data = sys.stdin.read()
    tokens = tokenize_input(input_data)
    result = process_tokens(tokens)
    print("\n".join(result))
