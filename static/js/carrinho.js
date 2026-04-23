function mostrar_carrinho()
{
    const resposta = await fetch("http://10.110.134.2:8080/api/get/carrinho")
    if (resposta.ok) {
        alert("ERRO")
    } else{
        const carrinho = document.getElementById("carrinho")
        carrinho.innerHTML = ""
        let total = 0
        for (let dado of dados){
            total = total + dado.preco
            let linha = ` 
            <div class="cart-item" style="display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-bottom: 15px; border-bottom: 1px solid #eee; padding-bottom: 10px;">
            
            <div style="display: flex; align-items: center; gap: 10px;">
                <img src="${dado.dados}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;">
                <div>
                    <p style="font-weight: bold; margin: 0; font-size: 0.9rem;">{{ item.nome }}</p>
                    <p style="color: var(--primary-red); margin: 0; font-size: 0.85rem;">R$ {{ item.preco }}</p>
                </div>
            </div>

            <a href="/remover/{{ loop.index0 }}" 
               class="material-symbols-outlined" 
               style="text-decoration: none; color: #999; font-size: 1.2rem; cursor: pointer; transition: color 0.2s;"
               onmouseover="this.style.color='red'" 
               onmouseout="this.style.color='#999'">
               delete
            </a>
        </div>
            `
            carrinho.innerHTML += linha
        }
    }
}