<template>
<div >
    <div class="shadow-lg rounded-lg overflow-hidden mx-4 md:mx-10">
        <div class="bg-white dark:bg-gray-800 p-8 rounded-lg shadow-md border dark:border-gray-700">
            <h1 class="text-2xl font-bold text-gray-800 dark:text-white mb-4">Receta Médica</h1>

            <!-- Información del Paciente -->
            <div class="mb-6">
                <h2 class="text-xl font-semibold text-gray-700 dark:text-white mb-2">Información del Paciente</h2>
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label for="nombre" class="block text-gray-700 dark:text-white mb-1">Nombre</label>
                        <input type="text" id="nombre" class="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none">
                    </div>
                    <div>
                        <label for="fecha" class="block text-gray-700 dark:text-white mb-1">Fecha</label>
                        <input type="date" id="fecha" class="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none">
                    </div>
                </div>

                <div class="mt-4">
                    <label for="peso" class="block text-gray-700 dark:text-white mb-1">Peso (kg)</label>
                    <input type="number" id="peso" class="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none">
                </div>

                <div class="mt-4">
                    <label for="talla" class="block text-gray-700 dark:text-white mb-1">Talla (m)</label>
                    <input type="number" id="talla" class="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none">
                </div>

                <div class="mt-4">
                    <label for="edad" class="block text-gray-700 dark:text-white mb-1">Edad</label>
                    <input type="number" id="edad" class="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none">
                </div>

                <div class="grid grid-cols-2 gap-4 mt-4">
                    <div>
                        <label for="presion_arterial" class="block text-gray-700 dark:text-white mb-1">Presión Arterial</label>
                        <input type="text" id="presion_arterial" class="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none">
                    </div>
                    <div>
                        <label for="diagnostico" class="block text-gray-700 dark:text-white mb-1">Diagnóstico</label>
                        <input type="text" id="diagnostico" class="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none">
                    </div>
                </div>

                <div class="mt-4">
                    <label for="prescripcion" class="block text-gray-700 dark:text-white mb-1">Prescripción Médica</label>
                    <textarea id="prescripcion" class="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none"></textarea>
                </div>
            </div>

            <div class="mt-8 flex justify-end">
                <button class="bg-teal-500 text-white px-4 py-2 rounded-lg hover:bg-teal-700 dark:bg-teal-600 dark:text-white dark:hover:bg-teal-900">Generar Receta</button>
            </div>
        </div>
    </div>
    <br><br>
</div>
<div class="shadow-lg rounded-lg overflow-hidden mx-4 md:mx-10">
    <table class="w-full table-fixed">
        <thead>
            <tr class="bg-gray-100">
                <th class="w-1/4 py-4 px-6 text-left text-gray-600 font-bold uppercase">Nombre</th>
                <th class="w-1/4 py-4 px-6 text-left text-gray-600 font-bold uppercase">Fecha</th>
                <th class="w-1/4 py-4 px-6 text-left text-gray-600 font-bold uppercase">Peso</th>
                <th class="w-1/4 py-4 px-6 text-left text-gray-600 font-bold uppercase">Talla</th>
                <th class="w-1/4 py-4 px-6 text-left text-gray-600 font-bold uppercase">Edad</th>
                <th class="w-1/4 py-4 px-6 text-left text-gray-600 font-bold uppercase">P.A</th>
                <th class="w-1/4 py-4 px-6 text-left text-gray-600 font-bold uppercase">Diagnostico</th>
                <th class="w-1/4 py-4 px-6 text-left text-gray-600 font-bold uppercase">Prescripción Médica</th>
            </tr>
        </thead>
        <tbody class="bg-white">
            <tr>
        <td class="py-4 px-6 border-b border-gray-200">John Doe</td>
        <td class="py-4 px-6 border-b border-gray-200 truncate">2024-06-10</td>
        <td class="py-4 px-6 border-b border-gray-200">75 kg</td>
        <td class="py-4 px-6 border-b border-gray-200">180 cm</td>
        <td class="py-4 px-6 border-b border-gray-200">35 años</td>
        <td class="py-4 px-6 border-b border-gray-200">120/80 mmHg</td>
        <td class="py-4 px-6 border-b border-gray-200">Hipertensión</td>
        <td class="py-4 px-6 border-b border-gray-200">Recetar medicamento X</td>
    </tr>
    <tr>
        <td class="py-4 px-6 border-b border-gray-200">Jane Doe</td>
        <td class="py-4 px-6 border-b border-gray-200 truncate">2024-06-11</td>
        <td class="py-4 px-6 border-b border-gray-200">68 kg</td>
        <td class="py-4 px-6 border-b border-gray-200">165 cm</td>
        <td class="py-4 px-6 border-b border-gray-200">40 años</td>
        <td class="py-4 px-6 border-b border-gray-200">130/90 mmHg</td>
        <td class="py-4 px-6 border-b border-gray-200">Diabetes</td>
        <td class="py-4 px-6 border-b border-gray-200">Recetar medicamento Y</td>
    </tr>
    <tr>
        <td class="py-4 px-6 border-b border-gray-200">John Smith</td>
        <td class="py-4 px-6 border-b border-gray-200 truncate">2024-06-12</td>
        <td class="py-4 px-6 border-b border-gray-200">80 kg</td>
        <td class="py-4 px-6 border-b border-gray-200">175 cm</td>
        <td class="py-4 px-6 border-b border-gray-200">45 años</td>
        <td class="py-4 px-6 border-b border-gray-200">140/95 mmHg</td>
        <td class="py-4 px-6 border-b border-gray-200">Obesidad</td>
        <td class="py-4 px-6 border-b border-gray-200">Recetar medicamento Z</td>
    </tr>
    <tr>
        <td class="py-4 px-6 border-b border-gray-200">Alice Johnson</td>
        <td class="py-4 px-6 border-b border-gray-200 truncate">2024-06-13</td>
        <td class="py-4 px-6 border-b border-gray-200">65 kg</td>
        <td class="py-4 px-6 border-b border-gray-200">170 cm</td>
        <td class="py-4 px-6 border-b border-gray-200">30 años</td>
        <td class="py-4 px-6 border-b border-gray-200">115/75 mmHg</td>
        <td class="py-4 px-6 border-b border-gray-200">Ninguno</td>
        <td class="py-4 px-6 border-b border-gray-200">Sin prescripción</td>
    </tr>
    <tr>
        <td class="py-4 px-6 border-b border-gray-200">Michael Brown</td>
        <td class="py-4 px-6 border-b border-gray-200 truncate">2024-06-14</td>
        <td class="py-4 px-6 border-b border-gray-200">70 kg</td>
        <td class="py-4 px-6 border-b border-gray-200">185 cm</td>
        <td class="py-4 px-6 border-b border-gray-200">50 años</td>
        <td class="py-4 px-6 border-b border-gray-200">125/85 mmHg</td>
        <td class="py-4 px-6 border-b border-gray-200">Colesterol alto</td>
        <td class="py-4 px-6 border-b border-gray-200">Recetar medicamento A</td>
    </tr>
    <tr>
        <td class="py-4 px-6 border-b border-gray-200">John Doe</td>
        <td class="py-4 px-6 border-b border-gray-200">2024-06-10</td>
        <td class="py-4 px-6 border-b border-gray-200">75 kg</td>
        <td class="py-4 px-6 border-b border-gray-200">180 cm</td>
        <td class="py-4 px-6 border-b border-gray-200">35 años</td>
        <td class="py-4 px-6 border-b border-gray-200">120/80 mmHg</td>
        <td class="py-4 px-6 border-b border-gray-200">Hipertensión</td>
        <td class="py-4 px-6 border-b border-gray-200">Recetar medicamento X</td>
    </tr>
    <tr>
        <td class="py-4 px-6 border-b border-gray-200">Jane Doe</td>
        <td class="py-4 px-6 border-b border-gray-200">2024-06-11</td>
        <td class="py-4 px-6 border-b border-gray-200">68 kg</td>
        <td class="py-4 px-6 border-b border-gray-200">165 cm</td>
        <td class="py-4 px-6 border-b border-gray-200">40 años</td>
        <td class="py-4 px-6 border-b border-gray-200">130/90 mmHg</td>
        <td class="py-4 px-6 border-b border-gray-200">Diabetes</td>
        <td class="py-4 px-6 border-b border-gray-200">Recetar medicamento Y</td>
    </tr>
    <tr>
        <td class="py-4 px-6 border-b border-gray-200">John Smith</td>
        <td class="py-4 px-6 border-b border-gray-200">2024-06-12</td>
        <td class="py-4 px-6 border-b border-gray-200">80 kg</td>
        <td class="py-4 px-6 border-b border-gray-200">175 cm</td>
        <td class="py-4 px-6 border-b border-gray-200">45 años</td>
        <td class="py-4 px-6 border-b border-gray-200">140/95 mmHg</td>
        <td class="py-4 px-6 border-b border-gray-200">Obesidad</td>
        <td class="py-4 px-6 border-b border-gray-200">Recetar medicamento Z</td>
    </tr>
    <tr>
        <td class="py-4 px-6 border-b border-gray-200">Alice Johnson</td>
        <td class="py-4 px-6 border-b border-gray-200">2024-06-13</td>
        <td class="py-4 px-6 border-b border-gray-200">65 kg</td>
        <td class="py-4 px-6 border-b border-gray-200">170 cm</td>
        <td class="py-4 px-6 border-b border-gray-200">30 años</td>
        <td class="py-4 px-6 border-b border-gray-200">115/75 mmHg</td>
        <td class="py-4 px-6 border-b border-gray-200">Ninguno</td>
        <td class="py-4 px-6 border-b border-gray-200">Sin prescripción</td>
    </tr>
    <tr>
        <td class="py-4 px-6 border-b border-gray-200">Michael Brown</td>
        <td class="py-4 px-6 border-b border-gray-200">2024-06-14</td>
        <td class="py-4 px-6 border-b border-gray-200">70 kg</td>
        <td class="py-4 px-6 border-b border-gray-200">185 cm</td>
        <td class="py-4 px-6 border-b border-gray-200">50 años</td>
        <td class="py-4 px-6 border-b border-gray-200">125/85 mmHg</td>
        <td class="py-4 px-6 border-b border-gray-200">Colesterol alto</td>
        <td class="py-4 px-6 border-b border-gray-200">Recetar medicamento A</td>
    </tr>
    <tr>
        <td class="py-4 px-6 border-b border-gray-200">Sophia Garcia</td>
        <td class="py-4 px-6 border-b border-gray-200">2024-06-15</td>
        <td class="py-4 px-6 border-b border-gray-200">60 kg</td>
        <td class="py-4 px-6 border-b border-gray-200">160 cm</td>
        <td class="py-4 px-6 border-b border-gray-200">25 años</td>
        <td class="py-4 px-6 border-b border-gray-200">110/70 mmHg</td>
        <td class="py-4 px-6 border-b border-gray-200">Ninguno</td>
        <td class="py-4 px-6 border-b border-gray-200">Sin prescripción</td>
    </tr>
            <!-- Add more rows here -->
        </tbody>
    </table>
</div>

</template>