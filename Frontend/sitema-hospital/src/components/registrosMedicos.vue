<template>
    <div class="flex flex-col md:flex-row justify-center items-center">
        
        <div class="w-max md:w-1/4 p-4">
            <div class="bg-white dark:bg-gray-800 p-8 rounded-lg shadow-md border dark:border-gray-700">
                <Recetas></Recetas>
            </div>
        </div>
    </div>

</template>

<script>

import Recetas from './recetaMedica.vue'

export default{
    components:{
        Recetas
    }
}
</script>