
def delimiter(input, output):
    with open(input, 'r') as input_file:
        with open(output, 'w') as output_file:
            # output_file.write(input_file.read().replace(',', '\t'))
            for line in input_file:
                row = []  # for accumulating the line
                curr = ''
                if_data = False
                for ch in line:
                    if ch == '"':
                        if_data = not if_data  # if we inside the "" or not
                        curr += ch
                    elif ch == ',' and not if_data:
                        row.append(curr)
                        curr = ''  # for the new column
                    else:
                        curr += ch  # other symbols
                row.append(curr.strip())  # add the last column
                output_file.write('\t'.join(row)+'\n')
            print("data is successfully added to ds.tsv")


if __name__ == '__main__':
    input = 'ds.csv'
    output = 'ds.tsv'
    delimiter(input, output)
