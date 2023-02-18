// fieldset 및 progressbar 요소 가져오기
var form = document.getElementById("msform");
var fieldsets = document.getElementsByTagName("fieldset");
var progressBar = document.getElementById("progressbar");
var progressList = progressBar.getElementsByTagName("li");

// 현재 위치를 추적하기 위한 변수
var current_fs, next_fs, previous_fs;
var currentProgress, nextProgress, previousProgress;
var currentIndex = 0;

// 다음 단계로 이동하는 함수
function next() {
  current_fs = fieldsets[currentIndex];
  next_fs = fieldsets[currentIndex + 1];

  currentProgress = progressList[currentIndex];
  nextProgress = progressList[currentIndex + 1];

  // form 유효성 검사
  if (currentIndex === 0 && !validateStep1()) {
    return;
  }

  // 필드셋 전환
  current_fs.style.display = "none";
  next_fs.style.display = "block";

  // progressbar 업데이트
  nextProgress.classList.add("active");

  // 현재 위치 업데이트
  currentIndex++;
}

// 이전 단계로 이동하는 함수
function previous() {
  current_fs = fieldsets[currentIndex];
  previous_fs = fieldsets[currentIndex - 1];

  currentProgress = progressList[currentIndex];
  previousProgress = progressList[currentIndex - 1];

  // 필드셋 전환
  current_fs.style.display = "none";
  previous_fs.style.display = "block";

  // progressbar 업데이트
  currentProgress.classList.remove("active");
  previousProgress.classList.add("active");

  // 현재 위치 업데이트
  currentIndex--;
}

// STEP1 폼 유효성 검사 함수
function validateStep1() {
  var feature1 = form.querySelector('input[name="feature1"]:checked');
  if (!feature1) {
    alert("성별을 선택해주세요.");
    return false;
  }
  return true;
}

// next 버튼 클릭 시 이벤트 리스너
var nextButtons = document.querySelectorAll(".next");
for (var i = 0; i < nextButtons.length; i++) {
  nextButtons[i].addEventListener("click", next);
}

// previous 버튼 클릭 시 이벤트 리스너
var previousButtons = document.querySelectorAll(".previous");
for (var i = 0; i < previousButtons.length; i++) {
  previousButtons[i].addEventListener("click", previous);
}
