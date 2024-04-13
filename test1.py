import streamlit as st
import requests

def get_option_chain(symbol, expiry_date):
    url = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}&expiryDate={expiry_date}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    # You can replace these cookies with your own. You may need to update them periodically.
    cookies = {
        'cookie1': 'defaultLang=en; _ga=GA1.1.759567813.1701852071; _ga_PJSKY6CFJH=GS1.1.1702017828.3.0.1702017828.60.0.0; _ga_QJZ4447QD3=GS1.1.1712835272.18.0.1712835272.0.0.0; nsit=4YYMxhmHdFlf8kUuez0B2NdM; AKA_A2=A; _abck=518DCC2692A9CDCFE5C7558C73CBA1F9~0~YAAQPJYRYPhPi8uOAQAA9hfD1gsphOfLOaozIhmwQ+UguvvK1mKbrqHIPlQGO+ohU3crv2M1LDxAZfeSsvKTQHxjT5hP1RYuWkPQbUQyghwDFh6BYCEB2CfvN7xt6NVzJK/ymzdqA4FNNvZa2ClqYn80oE7xr6DiniSCFpVUtKfelTR2+INv8F506BCYXoygb8RgSJ7vhKdDC+a0r9pRS7Jco6kFmyvQmo9ncBVJ9ubgfDt0D5A6HR3+a8dJu68ZW6SxY1otDBsJNk1Alz/K8BpBhnWFXpw5XBlmyg1KFuMQHrlwI68rxQ7Vk9qQhP2b+Np0kn2gpJPf0vNOmDd3YG6mdqX1Kqvyc7py8xPb5E116Fgudg0CBo83rkQxxMxe4/zNeQZQGYyHyeVQ4ue41cRd2WCYL0D7aQ==~-1~-1~-1; ak_bmsc=ABFFBC468CF283F1E507BF61D4D24D7B~000000000000000000000000000000~YAAQPJYRYJNQi8uOAQAAICPD1hd0ErRLlQtWORKibYNjFAYWVXLhwNNNJjjPEEwkuBfKGWOqmRlFj1pSdjeo0gp5C8oA9iN3JNYxrzZ8LlJItGlOCmHu7Z/FrGUiq3Bwx1g90d66wDFfgVNQ/BxNTR/aLcwrscVFKdkuGTNc+8VbVw46PHlZLmrkYfe5evIznBLVIi3O0yaTTop+OP0pnTPg4FDOxk1VRLPRI40g+b0CchMZuTrDvFw5cLwlRxw8Tsh5W9sIdCxl5h1bV7oNbeHkKhwR+ZYzsvcNEXWb4L8POtzCaNriJLzQKXZYNWKYg/oqz+ZkmUKlMvxO8Yq4kob17SJM0L7eYjI927PPKCuHTEaLnlXT8FeaurUJyH8NifE1QsrJChtBSNz/WkYRZHH7BbwS+iTbsdgmTmH6t1D6Rs89XGuG4pKdG6p5S8X1LKnkWs/KUVYm8ASzj1g=; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcxMzAwMDg2OCwiZXhwIjoxNzEzMDA4MDY4fQ.KfMfdUYlL1HA8dngdvZTqMVBGtMC37HWK27UcdpZK6A; bm_sz=D683A253030C380EDDAAE166EF1FED18~YAAQrwHVF+pAprqOAQAAnOzO1hf4DmXQutm5ijqFkj1o7KPHIkKI76LFn0hG34yCTDAA0xdBO4JcPKoZswGHPd7eZWarXgmWsfobE2MAzeB/gDOMXevhgV8/u9c0pipzVZW4/aHaqNoeMXArY2dPFXlySVzKJPE3wWpBz7PqcJqkKQprYN7+6TEoHi7syfzmzDk1iYj6Za8/NE55p531D+dpUNIWN56Jh5FfhPOw9mguZWKtwNsQCLlalnnj4wztclzVVD0/GPAaSE37sTNL8E3gUOytJc91QqxIyBKO7bJVQvxDxoLschK2XglQeQESPvuoyHB/TBMHp2gCblfq8YVYoWV08qYVPtHmeG/RF0la2STaUg4npiGEHJ6zr+UpLUO+oz5ZH69Q5/wsS9gJTznXPGpH/lQhJqdsE3Gk~3616816~4601650; _ga_87M7PJ3R97=GS1.1.1713000096.33.1.1713000871.0.0.0; bm_sv=2D4A6C2A9DF8C9DD981B9C0985F66713~YAAQrwHVFyDpprqOAQAAOjbY1hfCCbMgG5wgFPdCjgzJVuMe6/imXx5hcPaKHVemiD37QUbnRbLYeNTJ7aOhAzAelIdcdBOSMlXh3n4XvMS8geMiVBsdNO8lHu5JcVPTHBK3yj0PQ8eIDR81Ki+35Z1jUET6+I/JMwflxCeGLbgK5nk7n4t8GRPtrwhglI4qIc+45GEOzRyOUjt0Rzd7Cwi6O2gBwHevxffoOqoZSPAsbG202AN3HG+tYI/UeD+bs7iO~1; RT="sl=0&ss=luxwhlj4&tt=0&z=1&dm=nseindia.com&si=27dd24d2-ad9d-4caf-af2c-883121c5adf7&se=8c&bcn=%2F%2F684d0d42.akstat.io%2F&ul=dc8l"'
    }
    response = requests.get(url, headers=headers, cookies=cookies)
    data = response.json()
    return data['records']['data']

def main():
    st.title('NSE Option Chain Extractor for Nifty')

    # Select symbol
    symbol = st.text_input('Enter Nifty symbol (e.g., NIFTY)', 'NIFTY')

    # Select expiry date
    expiry_date = st.text_input('Enter expiry date (e.g., 31MAR2022)', '31MAR2022')

    # Fetch option chain
    option_chain = get_option_chain(symbol, expiry_date)

    if option_chain:
        # Display option chain data
        st.write(option_chain)
    else:
        st.write('Data not available')

if __name__ == "__main__":
    main()
