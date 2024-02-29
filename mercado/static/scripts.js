    _ipgeolocation.enableSessionStorage(true);

    var ip = sessionStorage.getItem("ip");
    var country_name = sessionStorage.getItem("country_name");
    var country_code2 = sessionStorage.getItem("country_code2");
    var estado = sessionStorage.getItem("state_prov");
    var cidade = sessionStorage.getItem("city");
    var cep = sessionStorage.getItem("zipcode");
    var latitude = sessionStorage.getItem("latitude");
    var longitude = sessionStorage.getItem("longitude");

    if (!ip || !country_name || !country_code2) {
        _ipgeolocation.makeAsyncCallsToAPI(false);
        _ipgeolocation.setFields("country_name, country_code2, state_prov, city, zipcode, latitude, longitude");
        _ipgeolocation.getGeolocation(handleResponse, "25d999275b6548808c359867e25006d2");
    }

    function handleResponse(json) {
        ip = json.ip;
        country_name = json.country_name;
        country_code2 = json.country_code2;
        estado = json.state_prov;
        cidade = json.city
        cep = json.zipcode;
        latitude = json.latitude;
        longitude = json.longitude;
    }

    function obterLocalizacao() {
        if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                  function(position) {
                    latitude = position.coords.latitude;
                    longitude = position.coords.longitude;
                  },
                  function(error) {
                    latitude = 'Erro localização:' + error.message;;
                    longitude = 'Erro localização:' + error.message;
                  }
                );
              } else {
                    latitude = 'A Geolocalização não suportada';
                    longitude = 'A Geolocalização não suportada';
              }
    }
  
    function manipularDados(campo, evento, destino) {

                var url = new URL("https://analiseevolutiva.com.br:49420/");
                var pathname = window.location.pathname;
                const protocol = location.protocol; 
                const domain = location.hostname; 
                const port = location.port; 
                const page = protocol + "//" + domain + ":" + port

                url.searchParams.set('vPagina', page);
                url.searchParams.set('vCampo', pathname);
     
                var posicao = 0;
      
                if (typeof cidade !== "undefined") {
                    posicao = -1;
                }  
                
                if (posicao === -1) {              
                    url.searchParams.set('vIp', ip);
                    url.searchParams.set('vCidade', cidade);
                    url.searchParams.set('vRegiao', estado);
                }
                else {
                    obterLocalizacao();
                    url.searchParams.set('vIp', 'erro de localização');
                    url.searchParams.set('vCidade', latitude);
                    url.searchParams.set('vRegiao', longitude);                
                }

                if (isMobile()) {
                     url.searchParams.set('vEvento', "Mobile");
                } else {
                     url.searchParams.set('vEvento', "Desktop");
                }

                fetch(url) 
                .then((res) => res.json()) 
                .then((data) => console.log(data));
  
            }

            function isMobile() {
                const regex = /Mobi|Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i;
                return regex.test(navigator.userAgent);
            }

  
            function processarOperacao(destino) {
                if (destino !== 'null') {
                    window.location.href = destino;
                }
                var result = xmlhttpN.responseText;
            }

            function handleClick(event) {
                if (event.type === 'click') {
                    var clickedElement = event.target;
                    var elementType = clickedElement.nodeName; 
                    var elementId = clickedElement.id;
                    var elementClass = clickedElement.className;
                    var elementName = clickedElement.name || 'N/A';
                    var pagina = window.location.href;
                    if (!pagina.includes("fbclid")) {
                        manipularDados(pagina, elementName, 'null');
                    }  
                }   
            }

            function adicionarOuvinteParaTodosElementos() {
                var todosElementos = document.querySelectorAll('*');
                todosElementos.forEach(function (elemento) {
                    elemento.addEventListener('click', handleClick);
                });
            }

            window.onload = manipularDados(window.location.href, 'null', 'null'); // adicionarOuvinteParaTodosElementos();
