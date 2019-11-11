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
    Ask JunyongPark
    ```
   
### data extract to csv & download image from Monde-data-server

##### 저장 형식은 left, top, bottom, origin_url, width, height : ltrb는 비율이 아닌 픽셀값 #####

```monde_data_extract.ipynb```
    
1. make instance
    ```
    $ extractmanager= DataExtractSave()
    $ imagedownloadmanager = S3DownloadManager()
    ```
2. make queryset
    > **queryset 은 CroppedImage 기반이어야 합니다.**
    ```
    $ queryset = CroppedImage.objects.filter(origin_source__image_review=True)
    ```
 
3. save_data_to_csv : 데이터 csv로 저장
    > save_data_to_csv('저장할 파일이름', 쿼리셋) --> **쿼리셋은 sliced 되면 오류가 납니다.(err: queryset = Queryset[:100])**
    > image 다운받을 때 다운받는 폴더는 미리 생성되어있어야 합니다. 
    ```    
    $ extractmanager.save_data_to_csv("20191106_tight_boxed_data.csv", queryset)
    $ imagedownloadmanager.download_s3_files_from_queryset('./data/', queryset)
    ```
    

### download S3 images to local [DEPRECATED] ###

```download_s3_files.ipynb```

##### s3에 업로드된 이미지들이 다른 bucket에 있어 두곳에서 다르게 다운받아야 함. csv와, 버킷 이름을 지정해 줘야 사용 가능합니다.


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
- [ ] data extract & download from Mondebro (web-crawler bucket data)
