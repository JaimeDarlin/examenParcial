function consultarProductoxTienda(idTienda)
{
    console.log(idTienda)
    fetch(`/consultaTienda/${idTienda}`)
    .then(response => response.json())
    .then(data => {
        nombreTiendaProductos = document.getElementById('nombreTiendaProductos')
        nombreTiendaProductos.innerHTML = data.direccion
        productosxtienda = document.getElementById('productosxtienda')
        productosxtienda.innerHTML = ''
        for(let i = 0; i < data.listaProductos.length; i++)
        {
            productosxtienda.innerHTML += `
            <tr>
                <td>${data.listaProductos[i][0]}</td>
                <td>${data.listaProductos[i][1]}</td>
                <td>${data.listaProductos[i][2]}</td>
                <td>${data.listaProductos[i][3]}</td>
            </tr>
            `
        }
    })
}