export default function DashboardPage() {
  return (
    <section className="space-y-6">
      <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
        <h1 className="text-2xl font-semibold">Dashboard</h1>
        <p className="mt-2 text-sm text-slate-600">
          Overview for your Instagram automation workflows.
        </p>
      </div>

      <div className="grid gap-4 md:grid-cols-3">
        {[
          { title: 'Messages', value: '0' },
          { title: 'Automations', value: '3' },
          { title: 'Replies Today', value: '0' },
        ].map((card) => (
          <div key={card.title} className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
            <p className="text-sm text-slate-500">{card.title}</p>
            <p className="mt-2 text-3xl font-semibold">{card.value}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
