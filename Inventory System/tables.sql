Create Table inventory_system.asset_valuation
(

    on_hand integer not null,
    asset_value numeric not null,
    code character varying(20) not null,
    date date not null,

    primary key(date, code)

)
