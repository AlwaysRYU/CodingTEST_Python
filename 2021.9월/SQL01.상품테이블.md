# 상품 정보를 저장할 수 있는 테이블 

```SQL
drop table Product;

# 상품 정보를 저장할 수 있는 테이블을 구성하는 쿼리
CREATE TABLE Product (
productCode INT PRIMARY KEY,
productName VARCHAR(16),
productPrice INT);

# 상품데이터를 5개 이상 저장하는 SQL
INSERT INTO Product (productCode, productName, productPrice)
	VALUES (1, "TV", 5000000),
			(2, "노트북", 1000000),
			(3, "헤드폰", 700000),
			(4, "선풍기", 40000),
			(5, "휴대폰", 2000000),
			(6, "텀블러", 25000),
            (7, "노트", 100);

# 15% 인하된 가격의 상품 정보를 출력한다.
SELECT productcode, productName, (productPrice * 0.85) "할인물품"
FROM Product;

# TV관련 상품을 20% 인하 하여 저장하고 출력
update Product
set productPrice = productPrice * 0.8
WHERE productCode = 1;

SELECT * 
FROM product;

# 총 금액
SELECT SUM(productPrice)
FROM product;

```