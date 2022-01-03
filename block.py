import json
import os
import hashlib



BLOCKCHAIN_DIR = "blockchain/"

def get_hash(previous_block):
    with open (BLOCKCHAIN_DIR+ previous_block, 'rb') as f:
        content = f.read()
    return hashlib.md5(content).hexdigest()

def check_integrity():
    ##getting hash of each block
    #start from second block as first one has no hash
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    results = []

    for file in files[1:3]:
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)

        prev_hash = block.get('previous_block').get(hash)
        prev_filename = block.get('previous_block').get('filename')

        actual_hash = get_hash(prev_filename)

        if prev_hash == actual_hash:
            res = 'ok'
        else:
            red = 'not ok'

        print(f'Block {prev_filename}: {res}')
        results.append({'block': prev_filename, 'result':res})
    return results
def write_block(data, timestamp):

    blocks_count = len( os.listdir(BLOCKCHAIN_DIR))
    previous_block = str(blocks_count)



    data_of_block = {
        "data":data,
    "timestamp":timestamp,
    "previous_block":{
        "hash":get_hash(previous_block),
        "filename":previous_block

    } 
    }

    current_block = BLOCKCHAIN_DIR + str(blocks_count) +1
    with open(current_block, 'w') as f:
        json.dump(data_of_block, f, indent=3, ensure_ascii=False)
        f.write('/n')

def main():
    write_block(data='h', timestamp='22')

if __name__=='__main__':
    main()
