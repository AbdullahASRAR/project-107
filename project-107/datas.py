import pandas as pd
import plotly.express as e
df=pd.read_csv("datas.csv")
mean=df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
fig=(e.scatter(mean,x="student_id",y="level",size="attempt",color="attempt"))
fig.show()