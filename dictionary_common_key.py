"""
dictionary common key
"""
dic1={"name":"mohsin","age":23,"dep":"cse"}
dic2={"name":"mullick","age":24,"dep":"eee"}
common_dictionary=set(dic1.keys())&set(dic2.keys())
print(f"Common keys: {common_dictionary}")