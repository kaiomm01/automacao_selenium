from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())



navegador = webdriver.Chrome(service = servico)

# passo 1: Acessando um site específico
url = 'https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M'
navegador.get(url)

# Passo 2:
# Procedimento para localizar o xpath: entre no site em questão, aperte com o botão direito do mouse e
# então em inspecionar. Vai aparecer o html da página, sendo que no canto esquerdo, na parte superior, 
# existe uma seta, clique nela. A partir daí, quando vc percorrer o site com o mouse, vai aparecer o 
# correspondente em html. Então encontre o elemmento que vc deseja, clique nele e então, com o botão direito
#, aperte em cima do html correspondente --> copy --> xpath

# Encontrando o elemento em Html e escrevendo meu nome
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys('Kaio')

# Encontrando o elemento em Html e escrevendo email
navegador.find_element('xpath', 
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys('kaiommartins2016@gmail.com')

# Encontrando o elemento em Html e escrevendo meu telefone
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys('91981140673')

# Encontrando o elemento e clicando nele
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button/span/b').click()