export default function AutomationsPage() {
  return (
    <section className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
      <h1 className="text-2xl font-semibold">Automations</h1>
      <p className="mt-2 text-sm text-slate-600">
        Configure keyword rules and reply templates.
      </p>
      <div className="mt-6 space-y-3">
        <div className="rounded-lg border border-slate-200 p-4">
          <p className="font-medium">Hello</p>
          <p className="text-sm text-slate-500">Replies with a friendly greeting.</p>
        </div>
        <div className="rounded-lg border border-slate-200 p-4">
          <p className="font-medium">Pricing</p>
          <p className="text-sm text-slate-500">Offers a link to pricing information.</p>
        </div>
      </div>
    </section>
  );
}
