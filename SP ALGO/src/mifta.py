panduan = browser.get('https://tokoperhutani.com/panduan')

bantuan = browser.get('https://tokoperhutani.com/faqs')

alamat = browser.get('https://tokoperhutani.com/article/detil/alamat-kantor')

browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/strong/li/a/strong').click()

browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/strong/li/ul/li[2]/a').clicl()

browser.find_element_by_name('user_pass1').send_keys('mifta@22')
browser.find_element_by_name('user_pass2').send_keys('mifta@22')

browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/li[1]/a/strong').click()
browser.find_element_by_id('email').send_keys('mifta896@gmail.com')
browser.find_element_by_id('password').send_keys("mifta@22")
browser.find_element_by_class_name('le-button').click()

browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/strong/li/a').click()
browser.find_element_by_link_text('Profile').click()

retail = browser.get('https://tokoperhutani.com/beranda')
wilayah = browser.find_element_by_id('wilayah').click()
plh_wilayah = browser.find_element_by_xpath('//*[@id="wilayah"]/option[4]').click()
kota = browser.find_element_by_id('kota').click()
plh_kota = browser.find_element_by_xpath('//*[@id="kota"]/option[3]').click()
tpk = browser.find_element_by_id('select_kota').click()
plh_tpk = browser.find_element_by_xpath('//*[@id="select_kota"]/option[3]').click()
cari = browser.find_element_by_id('i_submit').click()
ketersediaan = browser.find_element_by_xpath('/html/body/div/strong/div[8]/div/div/form/div/div[3]/div[2]/table/tbody/tr[1]/td[1]/input').click()

beli_sekarang = browser.find_element_by_xpath('/html/body/div/strong/div[8]/div/div/form/input').click()

lanjut_belanja = browser.find_element_by_xpath('/html/body/div[1]/strong/div[5]/div/div/div[3]/a/button').click()
bank_bri     = browser.find_element_by_xpath('/html/body/div/strong/section[2]/div/div[2]/div/div/form/div/ul/li[2]/label/img').click()
konfirmasi_pemesanan=browser.find_element_by_xpath('//*[@id="confirmOrder"]')

browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/strong/li/a').click()
browser.find_element_by_link_text('Pesanan').click()

tanggal_pesan = browser.find_element_by_xpath('/html/body/div/strong/div[6]/div[2]/section[2]/div/div/div[1]/form/div/div[3]/div[2]/table/tbody/tr/td[1]')
print('Tanggal Pesanan:',tanggal_pesan.text)
invoice = browser.find_element_by_xpath('/html/body/div/strong/div[6]/div[2]/section[2]/div/div/div[1]/form/div/div[3]/div[2]/table/tbody/tr/td[2]')
print('Invoice: ',invoice.text)
lokasi = browser.find_element_by_xpath
('/html/body/div/strong/div[6]/div[2]div[3]/div[2]/table/tbody/tr/td[3]')
print('Lokasi: ',lokasi.text)
volume = browser.find_element_by_xpath('/html/body/div/strong/div[6]/div[2]/section[2]/div/div/div[1]/form/div/div[3]/div[2]/table/tbody/tr/td[4]')
print('Voume: ',volume.text)
total_harga_rp = browser.find_element_by_xpath('/html/body/div/strong/div[6]/div[2]/section[2]/div/div/div[1]/form/div/div[3]/div[2]/table/tbody/tr/td[5]')
print('Total Harga: ',total_harga_rp.text)
saluran_bayar = browser.find_element_by_xpath('/html/body/div/strong/div[6]/div[2]/section[2]/div/div/div[1]/form/div/div[3]/div[2]/table/tbody/tr/td[6]')
print('Saluran Bayar: ',saluran_bayar.text)

from selenium import webdriver
from time import sleep
opsi = webdriver.firefox.options.Options()
opsi.headless = False
binary = webdriver.firefox.firefox_binary.Firefox
Binary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
cap = webdriver.common.desired_capabilities.
DesiredCapabilities().FIREFOX
cap['marionette'] = True
browser=webdriver.Firefox(options=opsi,capabilities
=cap,firefox_binary=binary)
web_pht = 'https://www.tokoperhutani.com/'
browser.get(web_pht)

#metutup navigasi
browser.find_element_by_xpath('//*[@id="bannerModal"]/div/div/div[1]/button').click()
#login
browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/li[1]/a/strong').click()
browser.find_element_by_id('email').send_keys
('mifta896@gmail.com')
browser.find_element_by_id('password').send_keys
("mifta@22")
browser.find_element_by_class_name('le-button').click()
#mengecek status user
status = browser.find_element_by_xpath('/html/body/div[1]/nav/div/div[2]/ul/strong/li/a/img').get_attribute("title")
print(status)