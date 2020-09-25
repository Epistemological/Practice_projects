
import csv
f = open('bilar.csv')
csv_f = csv.reader(f)

def convert_row(row):
   return """<Brand="%s">
   <Modell>%s</Modell>
   <Year>%s</Year>
   <Registration>%s</Registration>
   <Verdict>%s</Verdict>
</Brand>""" % (
   row.Brand, row.Modell, row.Year, row.Registration, row.Verdict)

print '\n'.join([convert_row(row) for row in data[]])
