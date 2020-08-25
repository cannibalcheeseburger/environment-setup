

# Making Readme.md

Readme = f"""

### Contact / Social Media

[![Github](https://raw.githubusercontent.com/srbcheema1/CheemaFy/master/myPlugins/extra_things/png_images/social/github.png)](https://github.com/srbcheema1/)
[![LinkedIn](https://raw.githubusercontent.com/srbcheema1/CheemaFy/master/myPlugins/extra_things/png_images/social/linkedin-48x48.png)](https://www.linkedin.com/in/srbcheema1/)
[![Facebook](https://raw.githubusercontent.com/srbcheema1/CheemaFy/master/myPlugins/extra_things/png_images/social/fb.png)](https://www.facebook.com/srbcheema/)


### Developed by

Developer / Author: [Srb Cheema](https://github.com/srbcheema1/)

"""

with open("README.md",'w') as R:
    R.writelines(Readme)

print(Readme)