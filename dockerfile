from izone/flask
COPY . /app
WORKDIR /app
EXPOSE 5555
ENTRYPOINT ["python3"]
CMD ["runserver.py"]
