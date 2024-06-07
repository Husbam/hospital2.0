<template>

        <div class="mx-auto">
		<div class="flex justify-center px-6 py-12">
			<!-- Row -->
			<div class="w-full xl:w-3/4 lg:w-11/12 flex">
	<form class="px-8 pt-6 pb-8 mb-4 bg-white dark:bg-gray-800 rounded">
    <div class="mb-4 md:flex md:justify-around">
							<div class="mb-4 md:mr-2 md:mb-0">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="email">
									Usuario
								</label>
								<input
									class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
									id="usuario"
									type="text"
									placeholder="usuario"
								/>
							</div>
							<div class="md:ml-2">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="lastName">
                                   Contraseña
                                </label>
								<input
                                    class="w-full px-3 py-2 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="contrasena"
                                    type="password"
                                    placeholder="Contraseña"
                                />
							</div>
                            <div class="md:ml-2">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="lastName">
                                   repetir Contraseña
                                </label>
								<input
                                    class="w-full px-3 py-2 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="re_contrasena"
                                    type="password"
                                    placeholder="Contraseña"
                                />
							</div>
						</div>
						<div class="mb-6 text-center"><RouterLink to="/dashboard">
							<button
                                class="w-full px-4 py-2 font-bold text-white bg-blue-500 rounded-full hover:bg-blue-700 dark:bg-blue-700 dark:text-white dark:hover:bg-blue-900 focus:outline-none focus:shadow-outline"
                                type="button"
                            >
                                Iniciar Sesion
                            </button>
						</RouterLink>
						</div>
						<hr class="mb-6 border-t" />
						<div class="text-center">
                            <router-link to="/personas">
							<a class="inline-block text-sm text-blue-500 dark:text-blue-500 align-baseline hover:text-blue-800"
								href="#">
								Crear Cuenta
							</a>
                        </router-link>
						</div>
					</form>
			</div>
		</div>
		</div>

</template>