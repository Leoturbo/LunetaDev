# LunetaDev

Pequeno site estático para a empresa LunetaDev. Esta versão foi ampliada para um site multi-página profissional com layout responsivo, SVGs animados e formulários.

Estrutura principal:

- `index.html` — página inicial
- `about.html` — sobre a empresa
- `services.html` — serviços oferecidos
- `contato.html` — formulário de contato (Formspree placeholder)
- `privacidade.html` — política de privacidade
- `css/styles.css` — estilos globais
- `js/main.js` — interações leves

Testar localmente: abra `index.html` no navegador ou rode um servidor estático (ex.: `npx http-server` no diretório do projeto).

Próximos passos: atualizar conteúdo real (textos e números), trocar o `action` do formulário para o serviço escolhido, otimizar `logo.png` (WebP/SVG) e ajustar SEO/Open Graph conforme necessidade.

Configurar formulário (Formspree):

1. Acesse https://formspree.io e crie um form (gratuito para começar).
2. Substitua o atributo `action` em `contato.html` por `https://formspree.io/f/SEU_ID_AQUI`.
3. Teste o envio abrindo `contato.html` localmente ou no deploy e enviando uma mensagem de teste.

Favicon e sitemap:
- `logo.png` está utilizado como favicon; para produção, converta para `favicon.ico` ou `favicon-32x32.png` e atualize o link no `head`.
- Atualize `sitemap.xml` substituindo `https://example.com` pelo domínio do site antes de enviar ao Google Search Console.
