

fromCity = "São paulo, SP"
toCity = "umberlandia, MG"

driver.get(f"https://www.google.com.br/maps/dir/{fromCity}/{toCity}")

resultado = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[2]/div').text
driver.save_screenshot(f"{fromCity}-{toCity}.png")

print(resultado)