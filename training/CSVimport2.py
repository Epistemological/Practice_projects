



import pandas as pd

def import_csv():
    bilar = pd.read_csv('bilar.csv', sep=';')
    return bilar
def func(row):
    xml = ['<item>']
    for field in row.index:
        xml.append('  <field name="{0}">{1}</field>'.format(field, row[field]))
    xml.append('</item>')
    final_xml = '\n'.join(xml)
    return(final_xml)
    #return '\n'.join(xml)

def write_csv(df):
    xml = '\n'.join(df.apply(func, axis=1))
    print(xml)
    with open('testfile.xml', "w") as f:
        f.write(xml)
    f.close()

def main():
    df = import_csv()
    write_csv(df)

main()