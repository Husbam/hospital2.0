<template>
    <div class="flex h-screen bg-indigo-700">
<div class="w-full max-w-xs m-auto bg-indigo-100 rounded p-5">   
      <header>
        <img class="w-20 mx-auto mb-5" src="https://img.icons8.com/fluent/344/year-of-tiger.png" />
      </header>   
      <form>
        <div>
          <label class="block mb-2 text-indigo-500" for="username">Usuario</label>
          <input class="w-full p-2 mb-6 text-indigo-700 border-b-2 border-indigo-500 outline-none focus:bg-gray-300" type="text" name="username">
        </div>
        <div>
          <label class="block mb-2 text-indigo-500" for="password">Contraseña</label>
          <input class="w-full p-2 mb-6 text-indigo-700 border-b-2 border-indigo-500 outline-none focus:bg-gray-300" type="password" name="password">
        </div>
        <div>
          <router-link to="/dashboard">         
          <input class="w-full bg-indigo-700 hover:bg-pink-700 text-white font-bold py-2 px-4 mb-6 rounded" type="submit">
        </router-link> 
        </div>       
      </form>  
      <footer>
        <router-link to="/usuarios">
        <a class="text-indigo-700 hover:text-pink-700 text-sm float-left" href="#">Usuarios</a>
      </router-link>
        <router-link to="/personas">
            <a class="text-indigo-700 hover:text-pink-700 text-sm float-right" href="#">Crear Cuenta</a>
        </router-link>
        <router-link to="/register">
            <a class="text-indigo-700 hover:text-pink-700 text-sm float-right" href="#">123</a>
        </router-link>
      </footer>   
    </div>
</div>
</template>