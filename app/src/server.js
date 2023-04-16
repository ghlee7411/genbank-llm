const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');
const app = express();
const PORT = process.env.PORT || 3001;

// 파일을 읽을 디렉토리
const filesDir = path.join(__dirname, 'public');

// 정적 파일 제공
app.use(express.static(path.join(__dirname, 'build')));

// 파일 목록 API
app.get('/files', (req, res) => {
  fs.readdir(filesDir, (err, files) => {
    if (err) {
      res.status(500).send({ error: '디렉토리를 읽는 중 오류가 발생했습니다.' });
      console.log(err);
    } else {
      res.json({ files });
      console.log(req)
    }
  });
});

// 파일 내용 API
app.get('/files/:fileName', (req, res) => {
  const filePath = path.join(filesDir, req.params.fileName);
  res.sendFile(filePath);
});

// 모든 요청을 index.html로 리디렉션
app.use(cors());
