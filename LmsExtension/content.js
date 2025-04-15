window.addEventListener('load', function() {
  // 페이지의 특정 요소를 찾아 새로운 버튼 추가
  const header = document.querySelector('header');  // 예시로 페이지의 헤더를 찾음
  if (header) {
    const newButton = document.createElement('button');
    newButton.textContent = '새로운 버튼';
    newButton.style.padding = '10px';
    newButton.style.margin = '10px';
    newButton.onclick = () => {
      alert('새로운 기능 실행!');
    };
    header.appendChild(newButton);  // 헤더에 버튼 추가
  }
});
