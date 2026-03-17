<aside>
  
# ***README - Transporte para mascotas***

*Esta aplicación consiste en que los usuarios, dueños de mascotas, puedan solicitar servicios de transporte seguro para sus mascotas de una manera fácil y económica. La aplicación se divide en cuatro partes fundamentales, donde se pueden observar las funciones y los datos requeridos de las personas que conforman la aplicación.* 

🌷 ***Requisitos de Usuario:** Donde podemos encontrar el registro único para nuevos usuarios con datos especificos solicitados como dueño y responsable econimico de la mascota, tambien datos de la mascota y caracteristicas fisicas como de comportamiento y salud.*

🐡 ***Requisitos de Conductor:** Donde podemos encontrar el registro único de personas que cumplan con las caracteristicas requeridas para ser empleados de la aplicación UberPaws! , datos personales y datos del vehiculo en el cual trabajan.* 

🦋 ***Requisitos de administrador:** Donde podemos encontrar como dueños de la aplicación los datos de todos los usuarios y conductores registrados, el dinero entrante y saliente de los viajes solicitados y el historial completo de viajes y comentarios. Además de la capacidad de aceptar o rechazar solicitudes de conductores aspirantes a empleados.*

**Seguridad:** Donde podemos encontrar todas las medidas de seguridad implementadas en l aplicación.

</aside>

# ***FLUJO - Transporte para mascotas***

*El sistema se divide en tres flujos operativos más los requerimientos de seguridad dentro de los tres flujos:*

*🐝 **Flujo del Usuario (Semanas 1–3):**
Registro → Registro de mascotas → Solicitud de viaje → Calificación*

*🐝 **Flujo del Conductor (Semanas 4–6)**
Registro → Registro del vehículo → Gestión de viajes → Calificación*

*🐝**Flujo del Administrador (Semana 7)**
Gestión de perfiles → Gestión de viajes → Supervisión y seguridad*

<aside>


# ***REQUERIMIENTOS USUARIOS - Personas dueñas de mascotas***

*🐞 **Registro:** Define quién es el usuario. Solicita nombre, correo, contraseña, número de contacto y cuántas mascotas tiene. Tambien solicita nombre, tamaño, raza, edad, vacunas, comportamiento, modo de transporte y estado actual de las mascotas.  Ya que el transporte debe definir quienes son sus pasajeros (Mascotas)  y  responsables economicos y el vehiculo se debe adecuar porque cada mascota tiene requisitos distintos que afectan precio, seguridad y logística.*

*🐇 **Viaje:**  El módulo de viaje reúne todo lo necesario para que el transporte de la mascota pueda realizarse. Primero se ingresan la dirección de origen y destino, lo que permite al sistema calcular los km y estimar el tiempo del viaje. Con esa distancia se genera un precio, pero tanto el conductor como el usuario pueden proponer su propio precio. El pago en efectivo debe ser confirmado por ambas partes para evitar incumplimientos.
El conductor decide si acepta o rechaza el viaje según las condiciones de la mascota, y el tipo de transporte varía según su tamaño, raza o edad. El usuario registra el estado en que la mascota entra y sale del vehículo para dejar registro. Durante el viaje, el conductor controla el proceso mediante tres acciones básicas: iniciar, cancelar o terminar el viaje.*

*🌿**Calificación:** Designa el usuario una calificación de 1 a 5 al conductor dependiendiendo de las circunstancias y condiciones en las que transporto el animal ademas ded comentarias sugerencias, inconvenientes o incluso daños ejecutados por el conductor.*

</aside>

<aside>
  
🌼# ***REQUERIMIENTOS CONDUCTORES - Vehiculos***

*🐞 **Registro:**  Se solicita los datos básicos del conductor, como nombre, apellido, correo, número de contacto y la creación de una contraseña, con el fin de validar su identidad dentro de la plataforma. Se registra la información del vehículo, incluyendo el modelo, la capacidad máxima, las placas y los documentos de propiedad, además de los papeles al día en aseguradoras e impuestos. También se exige el certificado de capacitación en conducción para garantizar que el conductor esté formalmente preparado.*

***🐧 Comentarios:** se incorpora un espacio para que el conductor registre observaciones sobre la mascota transportada, ya sea daños, comportamientos o inconvenientes ocurridos durante el viaje, de modo que quede constancia y se pueda determinar responsabilidad entre las partes.*

</aside>

<aside>
  
🌼# ***REQUERIMIENTOS ADMINISTRADORES - Dueños***

*🍃 **Funciones:**  El sistema administrativo permite editar la información de todos los perfiles, incluyendo usuarios, mascotas y conductores, y también ofrece la opción de eliminar cuentas cuando sea necesario. Desde este panel se pueden revisar los comentarios y calificaciones que los conductores dejan sobre los usuarios, así como habilitar funciones de comunicación como llamadas o mensajes entre ambas partes. También incluye un menú para elegir entre la gestión de usuarios o conductores.*

***🪷Viajes:** Se puede visualizar el historial de viajes realizados, cobros y métodos de pago. Además, el administrador puede aceptar o rechazar conductores registrados según su compatibilidad con el servicio, y cuenta con herramientas de seguimiento y vigilancia durante los viajes para garantizar control y seguridad.*

</aside>

<aside>
  
🌼# SEGURIDAD - Complementos

***🪷Seguridad:**  La seguridad del sistema reúne todas las funciones que garantizan que tanto usuarios como conductores puedan usar la plataforma sin riesgos y con información confiable. La aplicación debe mostrar claramente los datos del conductor y del vehículo para que, al llegar al punto de origen, el usuario pueda verificar que coinciden, y lo mismo ocurre a la inversa: el conductor también valida la identidad del pasajero. Además, el sistema registra la duración del viaje y compara el tiempo real con el estimado, mientras hace seguimiento de la ruta recorrida para asegurar que el trayecto sea el correcto.
También se incluye un botón de emergencia disponible tanto para el conductor como para el usuario, útil en caso de accidentes, desvíos sospechosos o cualquier inconveniente durante el recorrido. Para proteger la información, todos los perfiles deben contar con contraseña, y se implementan medidas de protección de datos personales junto con un sistema antifraude que evita suplantaciones o manipulaciones indebidas dentro de la plataforma.*

</aside>
