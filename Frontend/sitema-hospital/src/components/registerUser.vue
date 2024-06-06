<template>

<div class="h-full bg-gray-400 dark:bg-gray-900">
	<!-- Container -->
	<div class="mx-auto">
		<div class="flex justify-center px-6 py-12">
			<!-- Row -->
			<div class="w-full xl:w-3/4 lg:w-11/12 flex">
				<!-- Col -->
				<div class="w-full p-8 lg:w-1/2">
					<Personas/>
				</div>
				<div class="w-full p-8 lg:w-1/2">
					<Usuario/>
				</div>
			</div>
		</div>
	</div>
</div>
</template>
<script>
import Personas from './personas.vue'
import Usuario from './usuarios.vue'
export default{
	components:{
		Personas,
		Usuario
	}
}
</script>
