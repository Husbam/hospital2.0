<template>

        <div class="mx-auto">
		<div class="flex justify-center px-6 py-12">
			<!-- Row -->
			<div class="w-full xl:w-3/4 lg:w-11/12 flex">
                <form class="px-8 pt-6 pb-8 mb-4 bg-white dark:bg-gray-800 rounded">
						
						<div class="mb-4 md:flex md:justify-around">
							<div class="mb-4 md:mr-2 md:mb-0">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="email">
									NOMBRE
								</label>
								<input
									class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
									id="nombre"
									type="text"
									placeholder="Nombre"
								/>
							</div>
							<div class="md:ml-2">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="lastName">
                                   PRIMER APELLIDO
                                </label>
								<input
                                    class="w-full px-3 py-2 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="primer_apellido"
                                    type="text"
                                    placeholder="Apellido"
                                />
							</div>
                            <div class="md:ml-2">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="lastName">
                                   SEGUNDO APELLIDO
                                </label>
								<input
                                    class="w-full px-3 py-2 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="segundo_apellido"
                                    type="text"
                                    placeholder="Apellido"
                                />
							</div>
						</div>
						<div class="mb-4 md:flex md:justify-around">
							<div class="mb-4 md:mr-2 md:mb-0">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="password">
                                    CURP
                                </label>
								<input
                                    class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 dark:text-white border  rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="curp"
                                    type="text"
                                    placeholder="******************"
                                />
							</div>
							<div class="md:ml-2">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="c_password">
                                    Genero
                                </label>
								<form class="max-w-sm mx-auto">
                                    <select id="countries" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                        <option selected>Seleccione su Genero</option>
                                        <option value="">Hombre</option>
                                        <option value="">Mujer</option>
                                        <option value="">Otro</option>
                                    </select>
                                </form>
							</div>
                            <div class="md:ml-2">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="c_password">
                                    Tipo de Sangre
                                </label>
								<form class="max-w-sm mx-auto">
                                    <select id="countries" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                        <option selected>Seleccione su tipo de sangre</option>
                                        <option value="">A+</option>
                                        <option value="">A-</option>
                                        <option value="">B+</option>
                                        <option value="">B-</option>
                                        <option value="">0+</option>
                                        <option value="">0-</option>
                                        <option value="">AB+</option>
                                        <option value="">AB-</option>
                                    </select>
                                </form>
							</div>
						</div>
                        <div class="mb-4 md:flex md:justify-around">
							<div class="mb-4 md:mr-2 md:mb-0">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="email">
									Fecha de nacimiento
								</label>
								<input
									class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
									id="nombre"
									type="date"
									placeholder="00/00/0000"
								/>
							</div>
							<div class="md:ml-2">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="lastName">
                                   Telefono
                                </label>
								<input
                                    class="w-full px-3 py-2 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="telefono"
                                    type="text"
                                    placeholder="telefono"
                                />
							</div>
                            <div class="md:ml-2">
								<label class="block mb-2 text-sm font-bold text-gray-700 dark:text-white" for="lastName">
                                   Correo
                                </label>
								<input
                                    class="w-full px-3 py-2 text-sm leading-tight text-gray-700 dark:text-white border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="correo"
                                    type="email"
                                    placeholder="tu@correo.com"
                                />
							</div>
						</div>

						<div class="mb-6 text-center">
							<button
                                class="w-full px-4 py-2 font-bold text-white bg-blue-500 rounded-full hover:bg-blue-700 dark:bg-blue-700 dark:text-white dark:hover:bg-blue-900 focus:outline-none focus:shadow-outline"
                                type="button"
                            >
                                Crear Cuenta
                            </button>
						</div>
						<hr class="mb-6 border-t" />
						<div class="text-center">
                            <router-link to="/">
							<a class="inline-block text-sm text-blue-500 dark:text-blue-500 align-baseline hover:text-blue-800"
								href="#">
								Inicia sesion
							</a>
                        </router-link>
						</div>
					</form>
            </div>
        </div>
    </div>  
</template>