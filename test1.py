import streamlit as st
import requests

def get_option_chain(symbol, expiry_date):
    url = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}&expiryDate={expiry_date}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    cookies = {
        "Cookie": "_ga=GA1.1.759567813.1701852071; _ga_PJSKY6CFJH=GS1.1.1702017828.3.0.1702017828.60.0.0; _ga_QJZ4447QD3=GS1.1.1712835272.18.0.1712835272.0.0.0; nsit=4YYMxhmHdFlf8kUuez0B2NdM; _abck=518DCC2692A9CDCFE5C7558C73CBA1F9~0~YAAQPJYRYPhPi8uOAQAA9hfD1gsphOfLOaozIhmwQ+UguvvK1mKbrqHIPlQGO+ohU3crv2M1LDxAZfeSsvKTQHxjT5hP1RYuWkPQbUQyghwDFh6BYCEB2CfvN7xt6NVzJK/ymzdqA4FNNvZa2ClqYn80oE7xr6DiniSCFpVUtKfelTR2+INv8F506BCYXoygb8RgSJ7vhKdDC+a0r9pRS7Jco6kFmyvQmo9ncBVJ9ubgfDt0D5A6HR3+a8dJu68ZW6SxY1otDBsJNk1Alz/K8BpBhnWFXpw5XBlmyg1KFuMQHrlwI68rxQ7Vk9qQhP2b+Np0kn2gpJPf0vNOmDd3YG6mdqX1Kqvyc7py8xPb5E116Fgudg0CBo83rkQxxMxe4/zNeQZQGYyHyeVQ4ue41cRd2WCYL0D7aQ==~-1~-1~-1; ak_bmsc=ABFFBC468CF283F1E507BF61D4D24D7B~000000000000000000000000000000~YAAQPJYRYJNQi8uOAQAAICPD1hd0ErRLlQtWORKibYNjFAYWVXLhwNNNJjjPEEwkuBfKGWOqmRlFj1pSdjeo0gp5C8oA9iN3JNYxrzZ8LlJItGlOCmHu7Z/FrGUiq3Bwx1g90d66wDFfgVNQ/BxNTR/aLcwrscVFKdkuGTNc+8VbVw46PHlZLmrkYfe5evIznBLVIi3O0yaTTop+OP0pnTPg4FDOxk1VRLPRI40g+b0CchMZuTrDvFw5cLwlRxw8Tsh5W9sIdCxl5h1bV7oNbeHkKhwR+ZYzsvcNEXWb4L8POtzCaNriJLzQKXZYNWKYg/oqz+ZkmUKlMvxO8Yq4kob17SJM0L7eYjI927PPKCuHTEaLnlXT8FeaurUJyH8NifE1QsrJChtBSNz/WkYRZHH7BbwS+iTbsdgmTmH6t1D6Rs89XGuG4pKdG6p5S8X1LKnkWs/KUVYm8ASzj1g=; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcxMzAwMTk0NSwiZXhwIjoxNzEzMDA5MTQ1fQ.lwqeHE_H5jWQm9DQfDkRd09aJKHQjN75txGUllrogAY; bm_sz=D683A253030C380EDDAAE166EF1FED18~YAAQrwHVF0pmp7qOAQAAHFjf1heajy98heo8W2FB33KrNG0sr4qGs6FsjE6Q/i6fR106g8y95R+ViHZLHjB/nZo7Igpm8bjOciIoZzpOGFkxQlGXUS+VIeUxNQWDrDSOi+vEqGNl3dLgyHcsWXFcUWTLH9NLAGPo+P/rRyzmbIRu5W1xeEpYVvtAPDEnRbLe38fpwwcQYrhTjcdgF2tWDNdF2JQR+ZlDdI/cXPJbUx0lF0zHW/iHU3iZ9uOwdDXStMRlvuZzcxoT2AC3E8GAoxMOj4DWd0at069GJP6TXA3TEpexitAWROp/JpButrUXbJzYcoZ9V4MQBzeEfZ36xwrTojE4F2+LK/A5VMohgDqieBWfdXhEJiSDa7nnh6hIcmQwrON6N03Z0iPxtqGdU16TCJSKSoq/2hvF0xL5GVAK2wkAlVKzDCTtMn6B~3616816~4601650; _ga_87M7PJ3R97=GS1.1.1713000096.33.1.1713001947.0.0.0; bm_sv=2D4A6C2A9DF8C9DD981B9C0985F66713~YAAQPJYRYIIRjsuOAQAAMjcF1xemthRTOa0f9G3hLvDaAOmj1gMf/qeNQZPYLQLl+JKrWLnsIDXQu9pxD7Jh0p6mGNWFivQsJtcIMF7yFEGSCmE5zFMrFZ5iVl9LqEdyy5N66p/miBD9DD/lrhBY52vh6iFBSSPUdUI02108WpsVH8/4w4BEhQ48heYwrXq8s+Z/hc2T5AKa+DCqa9r2xC6OFCbvTEp2+ebGBFCfZJy0O3IzZ7Q5HN5/hrOTXAKg9ZjUsA==~1; RT="sl=0&ss=luxx4ntl&tt=0&z=1&dm=nseindia.com&si=27dd24d2-ad9d-4caf-af2c-883121c5adf7&se=8c&bcn=%2F%2F684d0d4c.akstat.io%2F&ul=1h8ye"
    }

    try:
        response = requests.get(url, headers=headers, cookies=cookies)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        st.error(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        st.error(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        st.error(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        st.error(f"An unexpected error occurred: {err}")

# Streamlit app code
st.title("Nifty Option Chain Extractor")

symbol = "NIFTY"  # Or any other index symbol
expiry_date = st.date_input("Select expiry date", value=datetime.date(2024, 4, 18))
if st.button("Get Option Chain"):
    option_chain_data = get_option_chain(symbol, expiry_date)
    if option_chain_data:
        st.write(option_chain_data)
