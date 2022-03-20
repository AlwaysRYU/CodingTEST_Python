# SQL 문제
### DB : countryDB
### JOIN관련 문제

```SQL
CREATE TABLE `customer` (
  `customer_id` int NOT NULL,
  `customer_nm` varchar(45) NOT NULL,
  PRIMARY KEY (`customer_id`)
);


CREATE TABLE `customer_order` (
  `order_id` int NOT NULL,
  `customer_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `order_price` int DEFAULT NULL,
  PRIMARY KEY (`order_id`)
);

CREATE TABLE `product` (
  `product_id` int NOT NULL,
  `product_nm` varchar(45) NOT NULL,
  `product_price` int DEFAULT NULL,
  PRIMARY KEY (`product_id`)
);

INSERT INTO `test`.`customer` (`customer_id`, `customer_nm`) VALUES ('1', '홍길동');
INSERT INTO `test`.`product` (`product_id`, `product_nm`, `product_price`) VALUES ('111', 'TV', '1000');
INSERT INTO `test`.`product` (`product_id`, `product_nm`, `product_price`) VALUES ('222', '냉장고', '2000');
INSERT INTO `test`.`customer_order` (`order_id`, `customer_id`, `product_id`, `order_price`) VALUES ('11', '1', '111', '1000');

SELECT *
FROM customer_order;
SELECT *
FROM customer_order, product;
-- 1 X 2 총 2개의 열개수

INSERT INTO `test`.`customer` (`customer_id`, `customer_nm`) VALUES ('2', '향단이');
SELECT * FROM CUSTOMER;
SELECT * FROM CUSTOMER, product, customer_order;

# JOIN 조건을 추가하기
SELECT *
FROM customer_order, customer, product
WHERE customer_order.customer_id = product.product_id;

SELECT *
FROM customer_order, customer, product
WHERE customer_order.customer_id = customer.customer_id 
AND customer_order.product_id = product.product_id;

SELECT *
-- 커스터머 기준으로 다나오게하고, 있으면 나오게하고 없으면 나오지 않게
FROM customer C LEFT OUTER JOIN customer_order CO
ON  C.customer_id = CO.customer_id;
-- ON은 연결고리임 이걸 기준으로
-- 주문하지 않은 향단이도 나온다.
-- 또는 컬럼이름이 같으면 USING() 을 써도 된다.

SELECT *
FROM customer C LEFT OUTER JOIN CUSTOMER_order CO
ON C.customer_id = CO.customer_id;


# 조인을 서브쿼리로 하기 
SELECT C.customer_id, C.customer_nm, P.product_nm
FROM customer_order CO, customer C, product P
WHERE CO.customer_id = C.customer_id
AND CO.product_id = P.product_id;

# 프러덕트nm을  서브쿼리로 출력하자
-- 메인 쿼리에서 해놓은 FROM 테이블을 사용할 수있다.
SELECT C.customer_id, C.customer_nm, ( SELECT P.product_nm FROM product P WHERE P.product_id = CO.product_id) "서브쿼리"
FROM customer_order CO, customer C
WHERE CO.customer_id = C.customer_id;

-- 밑의 오류
SELECT C.customer_id, C.customer_nm, ( SELECT P.product_nm FROM product P) "서브쿼리"
FROM customer_order CO, customer C
WHERE CO.customer_id = C.customer_id;


-- # 프롬절 서브쿼리 
SELECT C.customer_id, C.customer_nm, P.product_nm
FROM customer_order CO, customer C, (
	SELECT product_id, product_nm
    FROM product
    WHERE product_price <= 1500) P
WHERE CO.customer_id = C.customer_id
AND CO.product_id = P.product_id;

-- 밑 쿼리의 오류 : P.가 메인 FROM 절에서 선언되지 않아서 사용할 수 없다. 조건으로만 사용할 경우 SELECT절에 사용할 수 없다.
SELECT C.customer_id, C.customer_nm
FROM customer_order CO, customer C
WHERE CO.customer_id = C.customer_id
AND CO.product_id = (
	SELECT product_id
    FROM product P
    WHERE product_price <= 1500
    );
    

```