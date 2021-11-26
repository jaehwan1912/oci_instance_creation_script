# 이 블럭은 인스턴스 나열 API를 사용하는 부분입니다.
import requests
from oci.config import from_file
from oci.signer import Signer

def listit():
    # configuration file 불러오기
    config = from_file("<configuration_file_경로>", "DEFAULT")

    # request의 auth 부분 생성
    auth = Signer(
	      tenancy=config['tenancy'],
        user=config['user'],
        fingerprint=config['fingerprint'],
        private_key_file_location=config['key_file']
    )

    # endpoint
    endpoint = 'https://iaas.<region>.oraclecloud.com/20160918/instances/'

    # body
    body = {
      	"compartmentId":"<나열하기를 원하는 compartment의 OCID>"
    }

    # request 보내기, 해당 API는 get method를 요구합니다.
    response = requests.get(endpoint, params=body, auth=auth)
    
    # 대충 instance 갯수가 0인 compartment에 만들고 길이로 판별하겠습니다.
    return len(response.json())

def makeit():
    # configuration file 불러오기
    config = from_file("<configuration_file_경로>", "DEFAULT")

    # request의 auth 부분 생성
    auth = Signer(
	      tenancy=config['tenancy'],
        user=config['user'],
        fingerprint=config['fingerprint'],
        private_key_file_location=config['key_file']
    )

    # endpoint
    endpoint = 'https://iaas.<region>.oraclecloud.com/20160918/instances/'

    # body
    body = <훔쳐온 parameter(--data-raw 이후) 부분을 양 옆의 작은따옴표만 빼고 그대로 사용>

    # request 보내기, 해당 API는 post method를 요구합니다.
    response = requests.post(endpoint, json=body, auth=auth)
    
if __name__=='__main__':
    if listit() == 0:
        makeit()

    
