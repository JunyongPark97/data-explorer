# data-explorer #

download amazon s3 file

### How to install ###

- Install dependency :

    ```
    $ pip install -r requirements.txt
    ```

- Put `secret.json` file inside directory

    ```
    ...
    ```

### download S3 images to local ###

 - download_s3_files.ipynb
 
    ```
    $ s3manager = S3Manager()
    
    $ # s3manager.download_s3_files(s3bucket_name, s3bucket_directory_name, save_local_path, save_local_directory)
    $ # save_local_directory를 인식 못하는 경우도 있음 : 수정해주세요
    
    $ s3manager.download_s3_files('monde-data', 'cropped-bag-images-dev', './cropped_image.csv', 'data')
    ```

### download csv from Monde-data-server for object-detection ###

- monde_data_extract.ipynb

    ```
    $ # test_data_pd.to_csv(filename, mode, index=False)
    $ test_data_pd.to_csv("test_pd.csv", mode='w', index=False)
    ```

### TODO ###
- [ ] data extract to classification
