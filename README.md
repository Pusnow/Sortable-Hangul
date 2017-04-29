# Sortable-Hangul
정렬 가능한 한글(옛한글) 인코딩/인코더

## 기존 한글 인코딩의 문제점

### 정렬의 어려움


### 정렬 구현의 부재


## 해결 방안

### 새로운 인코딩

### Unicode PUA 사용


## PUA 할당
* Supplemental Private Use Area-A 를 사용
* 16비트
* 상위 1비트에 따라 두 블록로 나눠 사용
* *KS X 1026-1* 의 *An Order Table for Johab Hangul Consonant/Vowel Letters Table 을* 사용하여 미리 정렬된 코드 포인트를 사용

### 초성-중성 코드

<table>
<tr align="center" >
<th>19</th><th>18</th><th>17</th><th>16</th><th>15</th><th>14</th><th>13</th><th>12</th><th>11</th><th>10</th><th>9</th><th>8</th><th>7</th><th>6</th><th>5</th><th>4</th><th>3</th><th>2</th><th>1</th><th>0</th>
</tr>
<tr align="center">
<td>1</td><td>1</td><td>1</td><td>1</td><td>0 (Block)</td><td align="center" colspan=8>초성 정렬 코드 (8bits)</td><td  colspan=7>중성 정렬 코드 (7bits)</td>
</tr>
</table>


### 종성-타입 코드

<table>
<tr align="center">
<th>19</th><th>18</th><th>17</th><th>16</th><th>15</th><th>14</th><th>13</th><th>12</th><th>11</th><th>10</th><th>9</th><th>8</th><th>7</th><th>6</th><th>5</th><th>4</th><th>3</th><th>2</th><th>1</th><th>0</th>
</tr>
<tr align="center">
<td>1</td><td>1</td><td>1</td><td>1</td><td>1 (Block)</td><td align="center" colspan=8>종성 정렬 코드 (8bits)</td><td>0</td><td>0</td><td  colspan=2>방점 (2bits)</td><td  colspan=3>타입 정보 (3bits)</td>
</tr>
</table>

#### 타입 정보

* 000 : 일반 한글 코드 
* 001 : 반각 코드
* 010 : 한글 호환 자모
* 011 : 괄호 기호
* 100 : 원 기호
* 101 ~ 111 : 미할당

#### 방점
* 00 : 평성 (방점 없음)
* 01 : 거성 (방점 하나)
* 10 : 상성 (방점 둘)
* 11 : 미할당


## 한국어 유니코드
유니코드에는 한국어 단어로 되어 있는 몇 기호가 있다. ex) (오전) 321D

Korean 과 Hangul의 차이로 Korean 코드는 지원하지 않는다.