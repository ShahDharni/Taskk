import pandas as pd
import numpy as np

d=np.array(["Dharni","Dhruvi","Dhvani","Dharti"])
print("d :\n",d)

d1=pd.DataFrame(d)
print("DataFrame :\n",d1)


## Another Example
print()
d2={"Name":["Dharni","Dhruvi","Dhvani","Dharti"],
    "Age":[20,22,21,23]}
data=pd.DataFrame(d2)
print(data)