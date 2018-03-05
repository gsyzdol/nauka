

  import requests

  endpoint = "http://thecatapi.com/api/images/get"

  #get random cat image
  r = requests.get(edpoint, params= {'size'='small', 'type'='png'})

  #check the response status code
  print(r.status_code)

  #check generated url
  print(r.url)

  #read its contents
  img=r.content

  #display the image
  from IPython.display import Image
  Image(data=img)

  #save the response into file
  with open('cat_images/cat.png', 'wb') as f: f.write(img)