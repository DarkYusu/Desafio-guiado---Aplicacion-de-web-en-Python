from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
     return HttpResponse("""<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                              
                              <nav class="navbar navbar-expand-lg bg-dark">
                                <div class="container-fluid">
                                  
                                  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                                    <span class="navbar-toggler-icon"></span>
                                  </button>
                                  <div class="collapse navbar-collapse" id="navbarNav">
                                    <ul class="navbar-nav">
                                      <li class="nav-item">
                                        <a class="nav-link active text-light" aria-current="page" href="/">Inicio</a>
                                      </li>
                                      <li class="nav-item">
                                        <a class="nav-link text-light" href="/about">Sobre Nosotros</a>
                                      </li>
                                      <li class="nav-item">
                                        <a class="nav-link text-light" href="/contact">Contacto</a>
                                      </li>
                                    </ul>
                                  </div>
                                </div>
                              </nav>
                              <br>
                              <body class="bg-secondary">
                              <section class="px-5 m-0 border-0 bd-example m-0 border-0 bg-dark text-light">
                                <h1 class="fs-1">Inicio</2>
                                
                                <p class="fs-5 m-4">"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p>           
                              <div class="row row-cols-1 row-cols-md-3 g-3">
  <div class="col">
    <div class="card">
      <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnZuZDJ0NGNsYnByb2Izendrbnd4engwYzVpNmhzYnY3cHZjNXN5NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kFgzrTt798d2w/giphy.webp" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card">
      <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2V1Y2Q1a2MzMGE2OXcyZHE0YWljam0ybXp4bXd2aGhrN3NzczJoaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lW9XPLjNXyDDO/giphy.webp" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card">
      <img src="https://i.gifer.com/8aXh.gif" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
      </div>
    </div>
  </div>
</div>
</section>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>""")
                              
def contact(request):
      return HttpResponse("""<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                              <body class="bg-secondary">
                              <nav class="navbar navbar-expand-lg bg-dark">
                                <div class="container-fluid">
                                  
                                  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                                    <span class="navbar-toggler-icon"></span>
                                  </button>
                                  <div class="collapse navbar-collapse" id="navbarNav">
                                    <ul class="navbar-nav">
                                      <li class="nav-item">
                                        <a class="nav-link active text-light" aria-current="page" href="/">Inicio</a>
                                      </li>
                                      <li class="nav-item">
                                        <a class="nav-link text-light" href="/about">Sobre Nosotros</a>
                                      </li>
                                      <li class="nav-item">
                                        <a class="nav-link text-light" href="/contact">Contacto</a>
                                      </li>
                                    </ul>
                                  </div>
                                </div>
                              </nav>
                              <br>
                              <section class="p-5  m-0 border-0 bg-dark text-light">
                                <form>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    <div id="emailHelp" class="form-text text-info-emphasis">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1">
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
</section>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>""")
                              
def about(request):
    return HttpResponse("""<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                              <nav class="navbar navbar-expand-lg bg-dark ">
                                <div class="container-fluid">
                                  
                                  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                                    <span class="navbar-toggler-icon"></span>
                                  </button>
                                  <div class="collapse navbar-collapse" id="navbarNav">
                                    <ul class="navbar-nav">
                                      <li class="nav-item">
                                        <a class="nav-link active text-light" aria-current="page" href="/">Inicio</a>
                                      </li>
                                      <li class="nav-item">
                                        <a class="nav-link text-light" href="/about">Sobre Nosotros</a>
                                      </li>
                                      <li class="nav-item">
                                        <a class="nav-link text-light" href="/contact">Contacto</a>
                                      </li>
                                      
                                      </ul>
                                  </div>
                                </div>
                              </nav>
                              <br>
                              <body class="bg-secondary">
                              <section class="px-5 m-0 border-0 bd-example m-0 border-0 bg-dark text-light">
                                <h1 class="fs-1">Sobre Nosotros</2>
                                
                                <p class="fs-5 m-4">"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p>           
                              <div class="row row-cols-1 row-cols-md-3 g-3">
  <div class="col">
    <div class="card">
      <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXBmamk1bHltNzcxOTluaHZnMGFzZHE5cDQxd2V4OWYza3Vyc2RieiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wRvEvjCcuKBPy/giphy.webp" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card">
      <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExY25qYmlpeDhiN2U5cXkzeWk2M2M2YTR2dGF6ZW90dmtreGc3YmxwNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FkmpzRbsFE97q/giphy.webp" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card">
      <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGh0dXgyYjdtY3JweWVqbHlkYWxkbXRvaHhzdjYya3NuNGIyYWtnZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PMvwwKW3vMzss/giphy.webp" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
      </div>
    </div>
  </div>
</div>
</section>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>""")
                              
                              
                        