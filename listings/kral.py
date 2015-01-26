import kral

queries = ['android','bitcoin']

services = ['twitter','facebook']

for item in kral.stream(queries,services):
    print(item.service,item.text)
    