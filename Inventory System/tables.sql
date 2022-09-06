Create Table inventory_system.asset_valuation
(

    on_hand integer not null,
    asset_value numeric not null,
    code character varying(20) not null,
    date date not null,

    primary key(date, code)

)

Create Table inventory_system.shipping_status
(
    code_qb character varying(20),
    container_number integer not null,
    shipping_company character varying(50) not null,
    item_desc character varying(100) not null,
    cases integer,
    case_qty integer,
    est_deliv_date date,
    bol character varying (20),
    status character varying(20),
    notes character varying(50),
    shipping_status_id serial PRIMARY KEY

)

commit;
