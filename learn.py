import streamlit as st
import streamlit.components.v1 as components

def learn_page():
    lesson_menu = ["Lesson 1 - Solar System", "Lesson 2 - A sunny beach", "Lesson 3 - Flamingo and Tortoise"]
    lesson_choice = st.sidebar.selectbox("Choose Lesson", lesson_menu)

    match lesson_choice:
        case "Lesson 1 - Solar System":
            st.title("Lesson 1 - Solar System")
            components.html(
            """
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            <script type="text/javascript">
                function generate(prompt){
                console.log(prompt)
                const endpoint = 'https://api.openai.com/v1/images/generations';

                const data = {
                "model": "image-alpha-001",
                "prompt": prompt,
                "num_images": 1,
                "size": "256x256",
                "response_format": "url"
                };

                const headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer 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"
                };

                fetch(endpoint, {
                    method: 'POST',
                    headers: headers,
                    body: JSON.stringify(data)
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data.data[0].url);
                    const img = document.getElementById('dalle');
                    img.src = data.data[0].url;
    
                    // use the generated image URL
                })
                .catch(error => console.error(error));}
            </script>
            
            <style>
            span{   
                color: #007bff;
                cursor: pointer;
            }

            #dalleimage{
                display: flex;
                justify-content: center;
                align-items: center;
            }
            </style>

            <p>
                The solar system consists of the Sun and all the celestial objects that orbit it. It is located 
                in the <span onclick="generate(this.innerText)">Milky Way galaxy</span>, a spiral-shaped collection of stars and other astronomical objects. The Sun is 
                at the center of the solar system and makes up over 99 percent of its total mass. The eight planets of the 
                solar system, in order from the Sun, are <span onclick="generate(this.innerText)">Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune</span>. 
                These planets vary in size, composition, and distance from the Sun. In addition to the planets, the solar 
                system also includes dwarf planets, such as Pluto, and numerous smaller bodies such as <span onclick="generate(this.innerText)">asteroids and comets</span>. 
                The study of the solar system and its objects is called astronomy, and it has contributed greatly to our understanding 
                of the universe and our place in it.
            </p>
            </div>
            <br/>
            <div id="dalleimage">
            <img src="" id="dalle">
            </div>
            """, height=450,
        )
            
        # case "Lesson 2 - A sunny beach":
        #     st.title("Lesson 2 - A sunny beach")
        #     components.html(
        #     """
        #     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        #     <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        #     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        #     <script type="text/javascript">
        #         function generate(prompt){
        #         console.log(prompt)
        #         const endpoint = 'https://api.openai.com/v1/images/generations';

        #         const data = {
        #         "model": "image-alpha-001",
        #         "prompt": prompt,
        #         "num_images": 1,
        #         "size": "256x256",
        #         "response_format": "url"
        #         };

        #         const headers = {
        #         "Content-Type": "application/json",
        #         "Authorization": "Bearer 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"
        #         };

        #         fetch(endpoint, {
        #             method: 'POST',
        #             headers: headers,
        #             body: JSON.stringify(data)
        #         })
        #         .then(response => response.json())
        #         .then(data => {
        #             console.log(data.data[0].url);
        #             const img = document.getElementById('dalle');
        #             img.src = data.data[0].url;
    
        #             // use the generated image URL
        #         })
        #         .catch(error => console.error(error));}
        #         </script>
                
        #         <style>
        #         span{   
        #             color: #007bff;
        #             cursor: pointer;
        #         }

        #         #dalleimage{
        #             display: flex;
        #             justify-content: center;
        #             align-items: center;
        #         }
        #         </style>

        #         <p>
        #             The sun was blazing down on the sandy beach, as <span onclick="generate(this.innerText)">children ran and played in the waves</span>. 
        #             Seagulls cried overhead, as the smell of salty sea air mixed with the sweet scent of sunscreen. 
        #             It was a perfect day for soaking up the sun, and everyone was enjoying the warm, sunny paradise. The beach was buzzing with activity as families and friends 
        #             enjoyed the warm weather and the cool ocean breeze. Children splashed around in the waves while <span onclick="generate(this.innerText)">adults lounged on beach chairs</span>, 
        #             soaking up the sun.
        #         </p>
        #         </div>
        #         <br/>
        #         <div id="dalleimage">
        #         <img src="" id="dalle">
        #         </div>
        #         """, height=450,
        #     )
        # case "Lesson 3 - Flamingo and Tortoise":
        #     st.title("Lesson 3 - Flamingo and Tortoise")
        #     components.html(
        #     """
        #     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        #     <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        #     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        #     <script type="text/javascript">
        #         function generate(prompt){
        #         console.log(prompt)
        #         const endpoint = 'https://api.openai.com/v1/images/generations';

        #         const data = {
        #         "model": "image-alpha-001",
        #         "prompt": prompt,
        #         "num_images": 1,
        #         "size": "256x256",
        #         "response_format": "url"
        #         };

        #         const headers = {
        #         "Content-Type": "application/json",
        #         "Authorization": "Bearer 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"
        #         };

        #         fetch(endpoint, {
        #             method: 'POST',
        #             headers: headers,
        #             body: JSON.stringify(data)
        #         })
        #         .then(response => response.json())
        #         .then(data => {
        #             console.log(data.data[0].url);
        #             const img = document.getElementById('dalle');
        #             img.src = data.data[0].url;
    
        #             // use the generated image URL
        #         })
        #         .catch(error => console.error(error));}
        #         </script>
                
        #         <style>
        #         span{   
        #             color: #007bff;
        #             cursor: pointer;
        #         }

        #         #dalleimage{
        #             display: flex;
        #             justify-content: center;
        #             align-items: center;
        #         }
        #         </style>

        #         <p>
        #             In a far-off land, <span onclick="generate(this.innerText)">a curious flamingo met a wise old tortoise</span> who had seen many seasons come and go.
        #             They struck up a conversation and became fast friends, learning from each other's perspectives. 
        #             The <span onclick="generate(this.innerText)">flamingo taught the tortoise how to dance</span>, while the tortoise shared stories of the past. 
        #             As they spent time together, they realized that age and differences don't matter when it comes to 
        #             forming meaningful connections. In the end, they parted ways, but their friendship lasted forever, and they 
        #             looked forward to the day they would meet again.
        #         </p>
        #         </div>
        #         <br/>
        #         <div id="dalleimage">
        #         <img src="" id="dalle">
        #         </div>
        #         """, height=450,
        #     )
