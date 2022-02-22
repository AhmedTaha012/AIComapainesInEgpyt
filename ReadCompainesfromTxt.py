import pandas as pd
with open(r"E:\vscodes\.vscode\Companies.txt") as f:
    lines = f.readlines()
companies=[i.strip().replace(":","") for j,i in enumerate(lines) if i.endswith(":\n")]
domains=[i.strip().replace("- Interested in:","").replace(",","/") for j,i in enumerate(lines) if i.endswith(".\n")]
print(len(companies))
print(len(domains))
d = {'CompanyName': companies, 'CompanyDomin': domains}
df = pd.DataFrame(data=d)
df.to_csv("CompaniesofAiInEgypt.csv",index=False)
print(df)