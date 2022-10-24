import hashlib

# CREATE LIST PUBLIC DATASET IDS
public_ids = []
for i in range(256*512+1):
    st = str(i)+"test"
    public_ids.append( hashlib.md5(st.encode()).hexdigest() )
    
# DISPLAY FIRST 5 GENERATED
public_ids[:5]
