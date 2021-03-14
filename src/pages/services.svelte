
    <section class="hero is-medium" id="particles-js">
        <div class="hero-body" style="pointer-events: none;">
            <div class="container has-text-centered">
            <h1 class="title">
                Services
            </h1>
            <h2 class="subtitle is-size-4">
                    We offer a wide range of services, let's take a look.
            </h2><br><br>
            </div>
        </div>
    </section>



    <section class="hero is-dark is-medium speciality-section">
        <div class="hero-body">
            <div class="container has-text-centered">
                    <h1 class="title">
                        Specialities
                    </h1><br>
                <div class="columns is-centered">
                    
                    <div class="column pad-10 is-5" onmouseover="change_service_background(event,'1')">
                        <a href="/services/3d-printing"><img src="/static/images/services/1.jpg" class="hover-gray"></a>
                    </div>
                    <div class="column pad-10 is-5" onmouseover="change_service_background(event,'2')">
                        <a href="/services/ml-ai"><img src="/static/images/services/2.jpg" class="hover-gray"></a>
                    </div>
                </div>
                <div class="columns is-centered">
                    <div class="column pad-10 is-5" onmouseover="change_service_background(event,'3')">
                        <a href="#"><img src="/static/images/services/3.jpg" class="hover-gray"></a>
                    </div>
                    <div class="column pad-10 is-5" onmouseover="change_service_background(event,'4')">
                        <a href="#"><img src="/static/images/services/4.jpg" class="hover-gray"></a>
                    </div>
                </div>
            </div>
        </div>
    </section>


    <section class="section other-section" id="more-services">
        <div class="container has-text-centered"><br>
            <h1 class="is-size-3 has-text-weight-bold">
                Other Services
            </h1><br>

                    <a class="button is-rounded is-dark  other-link" onclick="other_service(event,'other-prototyping')" id="default-open-3">Prototyping</a>
                    <a class="button is-rounded is-dark  other-link" onclick="other_service(event,'other-multimedia')">Multimedia</a>
                    <a class="button is-rounded is-dark  other-link" onclick="other_service(event,'other-iot')">Internet of Things</a>
                    <a class="button is-rounded is-dark  other-link" onclick="other_service(event,'other-hardware')">Hardware</a>

                    <div class="columns is-centered">
                        <div class="column is-6 box" style="opacity:0.8;">
                            <div id="other-prototyping" class="other-content">
                                <br>
                                <h1 class="is-size-3">Prototyping</h1>
                                <br>
                                <p class="has-text-justified">The Prototyping Model is a systems development method (SDM) in which a prototype (an early approximation of a final system or product) is built, tested, and then reworked as necessary until an acceptable prototype is finally achieved from which the complete system or product can now be developed.</p>
                                <br>
                            </div>
                            <div id="other-multimedia" class="other-content">
                                <br>
                                <h1 class="is-size-3">Multimedia</h1>
                                <br>
                                <p class="has-text-justified">We've come a long way from instant pictures to moving pictures, or as we call it, videos, and to make a perfect video you need perfect editing, at Deshik, we do just that. So, let us help you perfectly document your visual content.</p>
                                <br>
                            </div>
                            <div id="other-iot" class="other-content">
                                <br>
                                <h1 class="is-size-3">Internet of Things</h1>
                                <br>
                                <p class="has-text-justified">The Internet of Things (IoT) is a system of interrelated computing devices, mechanical and digital machines, objects, animals or people that are provided with unique identifiers and the ability to transfer data over a network without requiring human-to-human or human-to-computer interaction.</p>
                                <br>
                            </div>
                            <div id="other-hardware" class="other-content">
                                <br>
                                <h1 class="is-size-3">Hardware</h1>
                                <br>
                                <p class="has-text-justified">Hardware is essential to run any software, it encompasses technology itself and we at Deshik, will help you build and modify your hardware requirements. Put your own spin on technology now!</p>
                                <br>
                            </div>
                        </div>
                    </div>
                    
            <br>
        </div>
    </section>


    <section class="hero is-primary overlap-bottom" id="fill-form">
        <div class="container hero-body has-text-centered"><br>
            <h1 class="title">
                Fill the Form
            </h1><br>
            <h2 class="is-size-5">Fill this simple form to find out information about the services we offer. <br>
            We will get back to you in no time.</h2>
        </div>
    </section>

    <section class="section">
        <div class="container has-text-centered">
            <div class="columns is-centered">
                <div class="column is-6 box">
                        <div class="typeform-widget" data-url="https://mridulganga.typeform.com/to/Es1Is6" style="width: 100%; height: 500px;"></div> <script> (function() { var qs,js,q,s,d=document, gi=d.getElementById, ce=d.createElement, gt=d.getElementsByTagName, id="typef_orm", b="https://embed.typeform.com/"; if(!gi.call(d,id)) { js=ce.call(d,"script"); js.id=id; js.src=b+"embed.js"; q=gt.call(d,"script")[0]; q.parentNode.insertBefore(js,q) } })() </script> <div style="font-family: Sans-Serif;font-size: 12px;color: #999;opacity: 0.5; padding-top: 5px;"> powered by <a href="https://admin.typeform.com/signup?utm_campaign=Es1Is6&utm_source=typeform.com-12801196-Basic&utm_medium=typeform&utm_content=typeform-embedded-poweredbytypeform&utm_term=EN" style="color: #999" target="_blank">Typeform</a> </div>
                    <form action="" class=" pad-10" hidden>
                        <div class="field">
                            <div class="control">
                                <input class="input" type="text" placeholder="Full name">
                            </div>
                        </div>
                        <div class="field">
                            <div class="control">
                                <input class="input" type="email" placeholder="Email Address">
                            </div>
                        </div>
                        <div class="field" >
                            <div class="control is-expanded">
                                <div class="select is-fullwidth">
                                    <select>
                                        <option selected disabled>Service Type</option>
                                        <option value="cloud">Cloud</option>
                                        <option value="android">Android</option>
                                        <option value="ml-ai">ML &amp; AI</option>
                                        <option value="3d-priting">3D Printing</option>
                                        <option value="3d-scanning">3D Scanning</option>
                                        <option value="multimedia">Multimedia</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="field">
                            <div class="control">
                                <textarea class="textarea" placeholder="Details"></textarea>
                            </div>
                        </div>
                        <button class="button is-fullwidth is-primary is-medium is-rounded is-outlined">Submit</button>

                    </form>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container has-text-centered"><br>
            <h1 class="title">
                How we do it
            </h1><br>
            <div class="columns is-centered">
                <div class="column is-8">
                    <img src="/static/images/services/process.jpg">
                </div>
            </div>
            
            
        </div>
    </section>

    <br><br>
