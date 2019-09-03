CURL COMMANDS To CALL API's & FETCH DATA FORM THE SERVER :
-----------------------------------------------------------


curl -i  https://bank-dir.herokuapp.com/api/

RESULT : 

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "branches/autocomplete": "https://bank-dir.herokuapp.com/api/branches/",
    "branches": "https://bank-dir.herokuapp.com/api/branches/"
}
---------------------------------------------------------

curl -i https://bank-dir.herokuapp.com/api/branches/


RESULT :

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 186194,
    "next": "https://bank-dir.herokuapp.com/api/branches/?page=2",
    "previous": null,
    "results": [
        {
            "url": "https://bank-dir.herokuapp.com/api/branches/3/",
            "ifsc": "ABHY0065001",
            "bank_id": 60,
            "branch": "RTGS-HO",
            "address": "ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024",
            "city": "MUMBAI",
            "district": "GREATER MUMBAI",
            "state": "MAHARASHTRA"
        },
        {
            "url": "https://bank-dir.herokuapp.com/api/branches/4/",
            "ifsc": "ABHY0065002",
            "bank_id": 60,
            "branch": "ABHYUDAYA NAGAR",
            "address": "ABHYUDAYA EDUCATION SOCIETY, OPP. BLDG. NO. 18, ABHYUDAYA NAGAR, KALACHOWKY, MUMBAI - 400033",
            "city": "MUMBAI",
            "district": "GREATER MUMBAI",
            "state": "MAHARASHTRA"
        },
        {
            "url": "https://bank-dir.herokuapp.com/api/branches/5/",
            "ifsc": "ABHY0065003",
            "bank_id": 60,
            "branch": "BAIL BAZAR",
            "address": "KMSPM'S SCHOOL, WADIA ESTATE, BAIL BAZAR-KURLA(W), MUMBAI-400070",
            "city": "MUMBAI",
            "district": "GREATER MUMBAI",
            "state": "MAHARASHTRA"
        },
        {
            "url": "https://bank-dir.herokuapp.com/api/branches/6/",
            "ifsc": "ABHY0065004",
            "bank_id": 60,
            "branch": "BHANDUP",
            "address": "CHETNA APARTMENTS, J.M.ROAD, BHANDUP, MUMBAI-400078",
            "city": "MUMBAI",
            "district": "GREATER MUMBAI",
            "state": "MAHARASHTRA"
        }
    ]
}

}
----------------------------------------------------------------------------------------

Assignment Statement For CURL command :  (1)

curl -i https://bank-directory.herokuapp.com/api/branches/autocomplete?q=RTGS&limit=3&offset=0

RESULT :

{
    "count": 67,
    "next": "https://bank-directory.herokuapp.com/api/branches/autocomplete/?limit=3&offset=0&page=2&q=RTGS",
    "previous": null,
    "results": [
        {
            "url": "https://bank-directory.herokuapp.com/api/branches/1/",
            "ifsc": "ABHY0065001",
            "bank_id": 60,
            "branch": "RTGS-HO",
            "address": "ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024",
            "city": "MUMBAI",
            "district": "GREATER MUMBAI",
            "state": "MAHARASHTRA"
        },
        {
            "url": "https://bank-directory.herokuapp.com/api/branches/116/",
            "ifsc": "ABNA0000001",
            "bank_id": 110,
            "branch": "RTGS-HO",
            "address": "414 EMPIRE COMPLEX, SENAPATI BAPAT MARG LOWER PAREL WEST MUMBAI 400013",
            "city": "MUMBAI",
            "district": "GREATER BOMBAY",
            "state": "MAHARASHTRA"
        },
        {
            "url": "https://bank-directory.herokuapp.com/api/branches/142/",
            "ifsc": "ADCB0000001",
            "bank_id": 143,
            "branch": "RTGS-HO",
            "address": "75, REHMAT MANZIL, V. N. ROAD, CURCHGATE, MUMBAI - 400020",
            "city": "MUMBAI",
            "district": "MUMBAI CITY",
            "state": "MAHARASHTRA"
        },
        {
            "url": "https://bank-directory.herokuapp.com/api/branches/143/",
            "ifsc": "ADCC0000001",
            "bank_id": 61,
            "branch": "RTGS-HO",
            "address": "THE AKOLA DISTRICT CENTRAL COOP. BANK LTD., P.B.NO. 8, CIVIL LINES, S.A. COLLEGE ROAD, AKOLA. 444001",
            "city": "AKOLA",
            "district": "AKOLA",
            "state": "MAHARASHTRA"
        }
    ]
}
--------------------------------------------------------------------------------------

Assignment Statement For CURL command :  (2)

curl -i http://bank-directory.herokuapp.com/api/branches/?q=Bangalore&limit=4&offset=0


RESULT :

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 23,
    "next": "http://bank-directory.herokuapp.com/api/branches/?limit=4&offset=0&page=2&q=Bangalore",
    "previous": null,
    "results": [
        {
            "url": "http://bank-directory.herokuapp.com/api/branches/93/",
            "ifsc": "ADCB0000002",
            "bank_id": 143,
            "branch": "BANGALORE",
            "address": "CITI CENTRE, 28, CHURCH STREET, OFF M. G. ROAD BANGALORE 560001",
            "city": "BANGALORE",
            "district": "BANGALORE URBAN",
            "state": "KARNATAKA"
        },
        {
            "url": "http://bank-directory.herokuapp.com/api/branches/124/",
            "ifsc": "ABNA0100318",
            "bank_id": 110,
            "branch": "BANGALORE",
            "address": "PRESTIGE TOWERS', GROUND FLOOR, 99 & 100, RESIDENCY ROAD, BANGALORE 560 025.",
            "city": "BANGALORE",
            "district": "BANGALORE URBAN",
            "state": "KARNATAKA"
        },
        {
            "url": "http://bank-directory.herokuapp.com/api/branches/6154/",
            "ifsc": "ANDB0002073",
            "bank_id": 15,
            "branch": "BANGALORE",
            "address": "BTM 4TH STAGE,929 BY A,4 TH STAGE,BTM LAYOUT,BANGALORE 560076",
            "city": "BANGALORE",
            "district": "BANGALORE",
            "state": "KARNATAKA"
        },
        {
            "url": "http://bank-directory.herokuapp.com/api/branches/6439/",
            "ifsc": "ANDB0002363",
            "bank_id": 15,
            "branch": "BANGALORE",
            "address": "NO 606,SYNDICATE BANK,ANDRAHALLI,MAIN ROAD,HERO HALLI,BANGALORE,560091",
            "city": "BANGALORE URBAN",
            "district": "BANGALORE URBAN",
            "state": "KARNATAKA"
        }
    ]
}
------------------------------------------------------------------------------------------