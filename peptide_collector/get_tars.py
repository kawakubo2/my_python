import os, requests, time

base_url = "https://tools.jpostdb.org/download/download.php?id={0}"
save_dir = "/temp/peptide/data" 
datasets_file = os.path.join(os.path.dirname(__file__), 'datasets.txt')

def main():
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    dataset_ids = get_dataset_ids(datasets_file)
    print(dataset_ids)
    for dataset_id in dataset_ids:
        download_dataset_tar_file(dataset_id)
        time.sleep(10)

def get_dataset_ids(datasets_file):
    with open(datasets_file, 'r', encoding="utf_8") as f:
        datasets = f.readlines()
        return [line.split('\t')[0] for line in datasets[1:]]
        
def download_dataset_tar_file(dataset_id):
    url = base_url.format(dataset_id)
    print(f"url={url}")
    response = requests.get(url)
    if not response.ok:
        print(f"ダウンロード失敗: {response.status_code} dataset_id={dataset_id}")
        return
    save_file = os.path.join(save_dir, dataset_id + '.tar')
    with open(save_file, 'wb') as out_f:
        out_f.write(response.content)
    print(f"保存: {save_file}")

if __name__ == '__main__':
    main()