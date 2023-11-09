const LaEmpresa = { template: '<div> Micromed System es una compañía fundada en Argentina en 1989, con destacada trayectoria en la industria ortopédica, especializándose en Artroscopía y Medicina del deporte. Su actividad central es el desarrollo, la fabricación y comercialización de productos biomédicos en la especialidad de Artroscopía y Traumatología. Cumple con los más altos y estrictos estándares de las normas de calidad y de servicio requeridos por el mercado regional e Internacional, las cuales garantizan la eficiencia y seguridad para alcanzar el más alto nivel en implantes osteointegrables. Sus recursos humanos, Profesionales altamente capacitados y en constante actualización, se orientan en una dedicada Atención al Cliente y comparten un real compromiso con la comunidad médica, la sociedad y el medio ambiente. Micromed System avanza sinérgicamente, sembrando y preservando la fluidez en las relaciones con sus Proveedores y Clientes, focalizándose continuamente en la ampliación y en el desarrollo de nuevas y mejores líneas de productos y servicios. La empresa se destaca en la rápida capacidad de respuesta a las necesidades de los mercados, un modelo comercial flexible y dinámico desarrollado por profesionales experimentados, alta competitividad en precios y gran capacidad de actualización e innovación. Micromed System, se ha consolidado en la región y, mediante constantes aportes de tecnología e inversión, ha alcanzado un sólido y reconocido prestigio el cual enorgullece plenamente a quienes formamos parte de esta prestigiosa organización.</div>' }

const routes = [
    { path: '/empresa', component: LaEmpresa }
]

const router = new VueRouter({
    routes
})

const app = new Vue({
    router,
    el: '#app'
})