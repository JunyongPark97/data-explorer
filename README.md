# data-explorer #

extract cropped 'ltrb' data

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
   
### download csv from Monde-data-server for object-detection ###

##### original_iamge의 image 저장 방식이 달라 다른 csv에 저장 #####
##### 저장 형식은 left, top, bottom, origin_url, width, height : ltrb는 비율이 아닌 픽셀값 #####

```monde_data_extract.ipynb```
    
1. make instance
    ```
    $ downloadmanager= DataExtractSave()
    ```
    
2. save_data_from_cropped : 크로링 박싱후 저장한 데이터 csv로 저장
    > save_data_from_cropped('저장할 파일이름', 쿼리셋 개수) --> **쿼리셋 개수는 비워두면 전체에 대해 다운로드**
    ```
    $ # Ex: save_data_from_cropped("crop_download_test.csv","")
    
    $ downloadmanager.save_data_from_cropped("crop_download_test.csv","3")
    ```
    
3. save_data_from_s3_temp : s3업로드 파일 박싱후 저장한 데이터 csv로 저장
    > save_data_from_s3_temp('저장할 파일이름', 쿼리셋 개수) --> 쿼리셋 개수는 비워두면 전체에 대해 다운로드
    ```
    $ # Ex: downloadmanager.save_data_from_s3_temp("s3upload_download_test.csv","")
    
    $ downloadmanager.save_data_from_s3_temp("s3upload_download_test.csv","3")
    ```

### download S3 images to local ###

```download_s3_files.ipynb```

##### s3에 업로드된 이미지들이 다른 bucket에 있어 두곳에서 다르게 다운받아야 함.


1. make instance
    ```
    $ s3manager = S3Manager()
    ```
    
2. download from monde-data : BucketNmae --> 크롤링 파일들 박싱한 데이터 저장한 버킷
    > s3manager.download_s3_files('버킷이름', ''폴더이름, 'csv파일', '저장경로')
    ```
    $ s3manager.download_s3_files('monde-data', 'original-bag-images-dev', './crop_download_test.csv', './data/')
    ```
    
3. download from temp-originalimage : BucketNmae --> hdf5파일들 저장한 버킷
    > s3manager.download_s3_files('버킷이름', ''폴더이름, 'csv파일', '저장경로') --> **폴더가 없으므로 비워둠**
    ```
    $ s3manager.download_s3_files('temp-originalimage', '', './s3upload_download_test.csv', './data/')
    ```

### TODO ###
- [ ] data extract to classification
