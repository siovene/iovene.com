date: 2013-02-27 15:08:08
slug: altering-all-sequence-owners-in-postgresql
title: Altering all sequence owners in Postgresql
categories: Software
tags: migration, mysql, postgresql

If you find yourself having to migrate from MySql to Postgresql, and you use
`mysql2psql` as suggested all over the Internet, mind that all the Postgresql
SEQUENCEs will be orphaned.

You may go and fix them one by one like this:

```sql
ALTER SEQUENCE foo_id_seq OWNED BY foo.id;
```

but that might take you forever. The following code will update all of them in
one go.

```sql
create function exec(text) returns text language plpgsql
 as $f$ begin execute $1; return $1; end; $f$;

select exec(format('alter sequence %s owned by %s.%I',
                   c.oid::regclass, a.attrelid::regclass, a.attname))
  from pg_class c
  join pg_depend d on (d.refobjid=c.oid and d.refclassid='pg_class'::regclass)
  join pg_attrdef ad on (d.objid=ad.oid and d.classid='pg_attrdef'::regclass)
  join pg_attribute a on (a.attrelid=ad.adrelid and a.attnum=ad.adnum)
 where c.relkind='S'
   and not exists(select * from pg_depend
                   where objid=c.oid and classid='pg_class'::regclass
                     and refclassid='pg_class'::regclass and refobjsubid>0
                     and deptype='a');
```

Remember to use transactions (`begin;` and `commit;`, or `rollback;` in case of
error), and to backup your database before attempting this. I'm not responsible
for your data losses.
